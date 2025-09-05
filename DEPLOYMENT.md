# Deployment Guide

## Backend Deployment on Render

1. **Push your code to GitHub:**
   ```bash
   git add .
   git commit -m "Prepare for deployment"
   git push origin main
   ```

2. **Deploy on Render:**
   - Go to [render.com](https://render.com) and sign up/login
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Use these settings:
     - **Name:** politician-classifier-api
     - **Environment:** Python 3
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `gunicorn --bind 0.0.0.0:$PORT server.server:app`
     - **Instance Type:** Free tier is fine for testing
   - Click "Create Web Service"
   - Wait for deployment (5-10 minutes)
   - Copy your Render URL (e.g., `https://politician-classifier-api.onrender.com`)

## Frontend Deployment on GitHub Pages

1. **Update the API URL:**
   - Open `UI/config.js`
   - Replace `your-render-app-name.onrender.com` with your actual Render URL

2. **Create a separate repository for the UI:**
   ```bash
   # Create a new repository on GitHub called "politician-classifier-ui"
   
   # In your local machine, create a new folder and copy UI contents
   cd ..
   mkdir politician-classifier-ui
   cd politician-classifier-ui
   
   # Copy all files from UI folder to this new directory
   Copy-Item -Path "c:\Users\Yaswanth Reddy\FamousPoliticianClassifier\UI\*" -Destination . -Recurse
   
   # Initialize git and push
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yaswanth33-ui/politician-classifier-ui.git
   git push -u origin main
   ```

3. **Enable GitHub Pages:**
   - Go to your GitHub repository settings
   - Scroll to "Pages" section
   - Select "Deploy from a branch"
   - Choose "main" branch and "/ (root)" folder
   - Click "Save"
   - Wait 5-10 minutes for deployment
   - Your site will be available at: `https://yaswanth33-ui.github.io/politician-classifier-ui/`

## Important Notes

1. **CORS:** The backend already has CORS enabled for all origins
2. **Free tier limitations:** 
   - Render free tier sleeps after 15 minutes of inactivity
   - First request after sleep may take 30-60 seconds
3. **Model files:** Ensure your `model.pkl` and `classes.json` are included in the repository
4. **Database:** SQLite database will be reset on each deployment on free tier

## Testing Deployment

1. Visit your GitHub Pages URL
2. Upload an image of a politician
3. Click "Classify"
4. The frontend should communicate with your Render backend

## Troubleshooting

- If backend fails: Check Render logs for errors
- If frontend can't connect: Verify the API URL in `config.js`
- If CORS errors: Ensure `flask-cors` is properly configured in backend
