import cv2
import mediapipe as mp
import subprocess
import time
import winsound

# ------------------ SPEAK FUNCTION (WINDOWS STABLE) ------------------
def speak(text):
    subprocess.Popen([
        "powershell",
        "-Command",
        f"Add-Type -AssemblyName System.Speech;"
        f"(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{text}')"
    ])

# ------------------ EMERGENCY FUNCTIONS ------------------
def emergency_beep():
    for _ in range(3):
        winsound.Beep(1200, 500)
        time.sleep(0.2)

def emergency_speak():
    for _ in range(5):
        speak("I need help")
        time.sleep(0.5)

# ------------------ CAMERA SETUP ------------------
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# ------------------ MEDIAPIPE SETUP ------------------
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    model_complexity=0,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)
mp_draw = mp.solutions.drawing_utils

# ------------------ VARIABLES ------------------
sentence = []
last_word = ""
last_sentence = ""
speak_armed = True
sentence_cooldown = 0
emergency_cooldown = 0
prev_time = 0

# ------------------ MAIN LOOP ------------------
while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    gesture = "None"
    hands_data = []

    if sentence_cooldown > 0:
        sentence_cooldown -= 1
    if emergency_cooldown > 0:
        emergency_cooldown -= 1

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            lm = hand_landmarks.landmark
            fingers = []

            fingers.append(1 if lm[4].x > lm[3].x else 0)
            for tip, joint in [(8,6),(12,10),(16,14),(20,18)]:
                fingers.append(1 if lm[tip].y < lm[joint].y else 0)

            hands_data.append(fingers)
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # ------------------ ONE HAND WORDS ------------------
        if len(hands_data) == 1:
            f = hands_data[0]

            if f == [0,0,0,0,0]:
                gesture = "SPEAK"
            elif f == [1,1,1,1,1]:
                gesture = "CLEAR"
            elif f == [1,1,1,0,0]:
                gesture = "Hi"
            elif f == [0,0,0,1,1]:
                gesture = "My"
            elif f == [0,0,0,0,1]:
                gesture = "Name is"
            elif f == [0,0,1,1,1]:
                gesture = "Sangram"
            elif f == [1,0,0,0,0]:
                gesture = "Yes"
            elif f == [0,1,1,0,0]:
                gesture = "Thank you"

            if gesture not in ["None", "SPEAK", "CLEAR"] and gesture != last_word:
                sentence.append(gesture)
                last_word = gesture

            if gesture == "SPEAK" and speak_armed and sentence:
                speak(" ".join(sentence))
                speak_armed = False

            if gesture == "CLEAR":
                sentence.clear()

            if gesture != "SPEAK":
                speak_armed = True

        # ------------------ TWO HAND SENTENCES ------------------
        if len(hands_data) == 2:
            h1, h2 = hands_data

            # 🚨 EMERGENCY: I NEED HELP
            if h1 == [0,0,0,0,0] and h2 == [1,1,1,1,1] and emergency_cooldown == 0:
                gesture = "I need help"
                emergency_beep()
                emergency_speak()
                emergency_cooldown = 200

            elif h1 == [1,1,1,1,1] and h2 == [1,1,1,1,1]:
                gesture = "Thank you very much"

            elif h1 == [1,0,0,0,0] and h2 == [1,0,0,0,0]:
                gesture = "Yes I understand"

            elif h1 == [0,1,1,0,0] and h2 == [0,1,1,0,0]:
                gesture = "Please help me"

            if gesture not in ["None", "I need help"] and gesture != last_sentence and sentence_cooldown == 0:
                speak(gesture)
                last_sentence = gesture
                sentence_cooldown = 40

    else:
        last_word = ""
        last_sentence = ""
        speak_armed = True

    # ------------------ FPS ------------------
    current_time = time.time()
    fps = int(1 / (current_time - prev_time)) if prev_time else 0
    prev_time = current_time

    frame = cv2.resize(frame, (900, 650))

    cv2.putText(frame, f"Gesture: {gesture}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.putText(frame, "Sentence: " + " ".join(sentence), (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,0), 2)

    cv2.putText(frame, f"FPS: {fps}", (20, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,255), 2)

    cv2.imshow("Gesture → Speech Translator (Emergency Ready)", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()