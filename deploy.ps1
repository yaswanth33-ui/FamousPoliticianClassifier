# Politician Classifier Deployment Script for Windows

Write-Host "=== Politician Classifier Deployment Script ===" -ForegroundColor Green
Write-Host ""

# Step 1: Commit and push backend changes
Write-Host "Step 1: Pushing backend code to GitHub..." -ForegroundColor Yellow
git add .
git commit -m "Prepare backend for Render deployment"
git push origin main

Write-Host "✅ Backend code pushed to GitHub" -ForegroundColor Green
Write-Host ""

# Step 2: Create UI deployment folder
Write-Host "Step 2: Preparing frontend for GitHub Pages..." -ForegroundColor Yellow

# Create deployment folder
$deployPath = "..\politician-classifier-ui-deploy"
if (Test-Path $deployPath) {
    Remove-Item $deployPath -Recurse -Force
}
New-Item -ItemType Directory -Path $deployPath -Force
Copy-Item -Path "UI\*" -Destination $deployPath -Recurse

Write-Host "✅ Frontend files copied to deployment folder" -ForegroundColor Green
Write-Host ""

Write-Host "=== Next Steps ===" -ForegroundColor Cyan
Write-Host "1. Deploy backend on Render:"
Write-Host "   - Go to https://render.com"
Write-Host "   - Create new Web Service"
Write-Host "   - Connect your GitHub repo"
Write-Host "   - Use Python environment"
Write-Host "   - Build command: pip install -r requirements.txt"
Write-Host "   - Start command: gunicorn --bind 0.0.0.0:`$PORT server.server:app"
Write-Host ""
Write-Host "2. Update frontend config:"
Write-Host "   - Edit $deployPath\config.js"
Write-Host "   - Replace 'your-render-app-name.onrender.com' with your Render URL"
Write-Host ""
Write-Host "3. Deploy frontend on GitHub Pages:"
Write-Host "   - Create new repo 'politician-classifier-ui'"
Write-Host "   - Push files from $deployPath to that repo"
Write-Host "   - Enable GitHub Pages in repo settings"
Write-Host ""
Write-Host "See DEPLOYMENT.md for detailed instructions!" -ForegroundColor Cyan
