// Configuration for the frontend
const CONFIG = {
    // Update this URL after deploying your backend to Render
    API_BASE_URL: window.location.hostname === 'localhost' 
        ? 'http://localhost:5000' 
        : 'https://your-render-app-name.onrender.com' // Replace with your actual Render URL
};
