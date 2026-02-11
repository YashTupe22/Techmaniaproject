# Hand Gesture Recognition - Sentence Builder

A modern web application that converts hand gestures into spoken sentences using real-time AI-powered hand tracking and text-to-speech synthesis.

## 🌟 Features

- **Real-time Hand Tracking**: Uses MediaPipe Hands for accurate gesture detection
- **Intuitive Interface**: Simple finger counting (1-4) to select words
- **Text-to-Speech**: Natural voice synthesis using Web Speech API
- **Responsive Design**: Works on desktop and mobile devices
- **Zero Backend**: Runs entirely in the browser
- **Accessibility Focused**: Designed for communication assistance

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ installed
- Modern web browser (Chrome, Edge, Firefox, or Safari)
- Webcam access

### Installation

1. **Clone or navigate to the project**:
   ```bash
   cd "e:\Tech Mania Project\web-app"
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Run development server**:
   ```bash
   npm run dev
   ```

4. **Open in browser**:
   Navigate to `http://localhost:3000`

## 📖 How to Use

### Building Sentences

1. **Show 1-4 Fingers**: Each finger count selects words from different categories
   - 1 Finger: Subjects (I, You, We, They, He, She)
   - 2 Fingers: Verbs (want, need, like, have, am, is)
   - 3 Fingers: Objects (water, food, help, rest, time, love)
   - 4 Fingers: Polite words (please, thank you, sorry, yes, no, okay)

2. **Show Palm (5 Fingers)**: Speak the complete sentence

3. **Clear Button**: Start over with a new sentence

### Tips for Best Results

- Ensure good lighting for better hand detection
- Keep your hand clearly visible in the camera frame
- Wait ~1 second between gestures
- Each finger count cycles through different words

## 🛠️ Technology Stack

- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **Hand Tracking**: MediaPipe Hands (JavaScript/WASM)
- **Text-to-Speech**: Web Speech API
- **Styling**: CSS Modules with modern design
- **Deployment**: Vercel

## 📦 Project Structure

```
web-app/
├── app/                      # Next.js app directory
│   ├── page.tsx             # Landing page
│   ├── layout.tsx           # Root layout
│   ├── globals.css          # Global styles
│   └── sentence-builder/    # Sentence builder page
├── components/              # React components
│   ├── HandTracker.tsx      # Camera and hand tracking
│   ├── WordSelector.tsx     # Word selection UI
│   ├── SentenceDisplay.tsx  # Sentence display and controls
│   └── Instructions.tsx     # Usage instructions
├── lib/                     # Core libraries
│   ├── handTracking.ts      # MediaPipe integration
│   ├── sentenceBuilder.ts   # Sentence logic
│   └── textToSpeech.ts      # TTS engine
├── package.json             # Dependencies
├── next.config.js           # Next.js configuration
├── tsconfig.json            # TypeScript configuration
└── vercel.json              # Vercel deployment config
```

## 🚀 Deployment to Vercel

### Option 1: Deploy via Vercel CLI

1. **Install Vercel CLI**:
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**:
   ```bash
   vercel login
   ```

3. **Deploy**:
   ```bash
   vercel
   ```

4. **Deploy to production**:
   ```bash
   vercel --prod
   ```

### Option 2: Deploy via Vercel Dashboard

1. Go to [vercel.com](https://vercel.com)
2. Click "Add New Project"
3. Import your Git repository
4. Vercel will auto-detect Next.js
5. Click "Deploy"

### Important Notes

- **HTTPS Required**: Camera access requires HTTPS (Vercel provides this automatically)
- **Browser Permissions**: Users must grant camera access
- **Browser Compatibility**: Best on Chrome/Edge, works on Firefox/Safari

## 🔧 Development

### Build for Production

```bash
npm run build
```

### Type Checking

```bash
npm run type-check
```

### Linting

```bash
npm run lint
```

## 🎯 Use Cases

- **Communication Assistance**: Help individuals with speech difficulties
- **Sign Language Learning**: Interactive learning tool
- **Accessibility**: Alternative input method
- **Demonstrations**: Educational and presentation purposes
- **Interactive Installations**: Public displays and exhibits

## 🤝 Contributing

This is a college project (Tech Mania Project). Contributions and suggestions are welcome!

## 📄 License

This project is created for educational purposes.

## 🙏 Acknowledgments

- MediaPipe team for the hand tracking library
- Next.js team for the amazing framework
- Web Speech API for text-to-speech capabilities

## 📞 Support

For issues or questions, please refer to the documentation or create an issue in the repository.

---

**Built with ❤️ by Tech Mania Project**
