#!/bin/bash

echo "=== Politician Classifier Deployment Script ==="
echo ""

# Step 1: Commit and push backend changes
echo "Step 1: Pushing backend code to GitHub..."
git add .
git commit -m "Prepare backend for Render deployment"
git push origin main

echo "✅ Backend code pushed to GitHub"
echo ""

# Step 2: Create UI deployment folder
echo "Step 2: Preparing frontend for GitHub Pages..."

# Create deployment folder
mkdir -p ../politician-classifier-ui-deploy
cp -r UI/* ../politician-classifier-ui-deploy/

echo "✅ Frontend files copied to deployment folder"
echo ""

echo "=== Next Steps ==="
echo "1. Deploy backend on Render:"
echo "   - Go to https://render.com"
echo "   - Create new Web Service"
echo "   - Connect your GitHub repo"
echo "   - Use Python environment"
echo "   - Build command: pip install -r requirements.txt"
echo "   - Start command: gunicorn --bind 0.0.0.0:\$PORT server.server:app"
echo ""
echo "2. Update frontend config:"
echo "   - Edit ../politician-classifier-ui-deploy/config.js"
echo "   - Replace 'your-render-app-name.onrender.com' with your Render URL"
echo ""
echo "3. Deploy frontend on GitHub Pages:"
echo "   - Create new repo 'politician-classifier-ui'"
echo "   - Push files from ../politician-classifier-ui-deploy/ to that repo"
echo "   - Enable GitHub Pages in repo settings"
echo ""
echo "See DEPLOYMENT.md for detailed instructions!"
