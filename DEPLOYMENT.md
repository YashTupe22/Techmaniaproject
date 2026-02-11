# Deployment Guide - Vercel

This guide will help you deploy the Hand Gesture Recognition app to Vercel.

## Prerequisites

- A Vercel account (free tier works fine)
- Git repository (GitHub, GitLab, or Bitbucket)
- Node.js 18+ installed locally

## Method 1: Deploy via Vercel Dashboard (Recommended)

### Step 1: Push to Git Repository

1. Initialize git in your project (if not already done):
   ```bash
   cd "e:\Tech Mania Project\web-app"
   git init
   git add .
   git commit -m "Initial commit - Hand Gesture Recognition App"
   ```

2. Create a new repository on GitHub/GitLab/Bitbucket

3. Push your code:
   ```bash
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

### Step 2: Import to Vercel

1. Go to [vercel.com](https://vercel.com) and sign in
2. Click "Add New..." → "Project"
3. Import your Git repository
4. Vercel will automatically detect Next.js settings
5. Click "Deploy"

### Step 3: Configure (if needed)

Vercel should auto-detect everything, but verify:
- **Framework Preset**: Next.js
- **Build Command**: `npm run build`
- **Output Directory**: `.next`
- **Install Command**: `npm install`

### Step 4: Deploy

Click "Deploy" and wait for the build to complete (usually 1-2 minutes).

## Method 2: Deploy via Vercel CLI

### Step 1: Install Vercel CLI

```bash
npm install -g vercel
```

### Step 2: Login

```bash
vercel login
```

### Step 3: Deploy

Navigate to your project directory:
```bash
cd "e:\Tech Mania Project\web-app"
```

Deploy to preview:
```bash
vercel
```

Deploy to production:
```bash
vercel --prod
```

## Post-Deployment

### Testing Your Deployment

1. Open the deployment URL provided by Vercel
2. Grant camera permissions when prompted
3. Test hand gesture recognition
4. Verify text-to-speech functionality

### Important Notes

✅ **HTTPS is Automatic**: Vercel provides HTTPS by default (required for camera access)

✅ **Camera Permissions**: Users must grant camera access in their browser

✅ **Browser Compatibility**: 
- ✅ Chrome/Edge (Recommended)
- ✅ Firefox
- ✅ Safari (may have limited MediaPipe support)
- ❌ Internet Explorer (not supported)

### Custom Domain (Optional)

1. Go to your project settings in Vercel
2. Navigate to "Domains"
3. Add your custom domain
4. Follow DNS configuration instructions

## Troubleshooting

### Build Fails

**Issue**: Build fails with module errors
**Solution**: Ensure all dependencies are in `package.json`:
```bash
npm install
npm run build  # Test locally first
```

### Camera Not Working

**Issue**: Camera doesn't load on deployed site
**Solution**: 
- Ensure you're accessing via HTTPS (Vercel does this automatically)
- Check browser permissions
- Try a different browser (Chrome recommended)

### MediaPipe Loading Issues

**Issue**: MediaPipe models fail to load
**Solution**: The app uses CDN for MediaPipe files. Ensure:
- CORS headers are set (already configured in `vercel.json`)
- Network allows CDN access

### Performance Issues

**Issue**: App is slow or laggy
**Solution**:
- Ensure good lighting for better detection
- Close other camera-using applications
- Try a different browser
- Check internet connection

## Environment Variables

This app doesn't require environment variables, but if you add any:

1. Go to Project Settings → Environment Variables
2. Add your variables
3. Redeploy for changes to take effect

## Monitoring

Vercel provides:
- **Analytics**: View traffic and performance
- **Logs**: Check runtime logs for errors
- **Deployment History**: Rollback if needed

Access these in your Vercel dashboard under your project.

## Updating Your Deployment

### Automatic Deployments

Once connected to Git, Vercel automatically deploys:
- **Production**: Pushes to `main` branch
- **Preview**: Pushes to other branches or pull requests

### Manual Deployments

Using Vercel CLI:
```bash
vercel --prod
```

## Cost

The free tier includes:
- Unlimited deployments
- 100GB bandwidth/month
- Automatic HTTPS
- Preview deployments

This is more than enough for this project!

## Next Steps

1. ✅ Deploy your app
2. ✅ Test all features
3. ✅ Share the URL
4. ✅ (Optional) Add custom domain
5. ✅ (Optional) Enable analytics

---

**Need Help?**
- Vercel Documentation: https://vercel.com/docs
- Next.js Documentation: https://nextjs.org/docs
- MediaPipe Documentation: https://google.github.io/mediapipe/

**Deployment Complete! 🎉**
