# Streamlit Deployment Guide

## 📋 Prerequisites
- GitHub account
- Streamlit Cloud account
- Your project pushed to GitHub

---

## 🚀 Step-by-Step Deployment

### Step 1: Push Your Project to GitHub
1. Initialize git (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit - HOTS Question Generator"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/hots-question-generator.git
   git push -u origin main
   ```

2. Replace `YOUR_USERNAME` with your actual GitHub username

### Step 2: Create a Streamlit Cloud Account
1. Go to https://streamlit.io/cloud
2. Click "Sign Up"
3. Connect your GitHub account
4. Authorize Streamlit to access your repositories

### Step 3: Deploy Your App
1. In Streamlit Cloud dashboard, click "New app"
2. Select:
   - **Repository**: Select your `hots-question-generator` repo
   - **Branch**: `main`
   - **Main file path**: `streamlit_app.py`

3. Click "Deploy"

### Step 4: Wait for Deployment
- Streamlit will install dependencies and deploy your app
- You'll get a public URL like: `https://your-app-name.streamlit.app`
- Share this URL with your teacher!

---

## 🔗 Sharing with Your Teacher

Once deployed, you can share the link in several ways:

1. **Direct Link**: Copy the URL and send it to your teacher
2. **Email**: Include the link in an email
3. **LMS/Classroom**: Post it on Google Classroom, Moodle, etc.
4. **QR Code**: Generate a QR code from the URL

---

## 📝 .gitignore File

Create a `.gitignore` file in the root directory with:
```
uploads/
__pycache__/
*.pyc
.DS_Store
.env
```

---

## 🐛 Troubleshooting

### If deployment fails:
1. Check that `streamlit_app.py` exists in the root directory
2. Ensure all dependencies are in `requirements.txt`
3. Check the deployment logs for errors
4. Verify that the file paths in imports are correct

### If the app doesn't work as expected:
1. Check Streamlit Cloud logs (Library menu → Manage app → View logs)
2. Ensure all utility files are in the correct location
3. Test locally first with: `streamlit run streamlit_app.py`

---

## 🔄 Updating Your App

To update the deployed app:
1. Make changes to your files locally
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Your update message"
   git push
   ```
3. Streamlit Cloud will automatically redeploy!

---

## 📦 Local Testing (Optional)

Before deploying, test locally:
```bash
pip install streamlit
streamlit run streamlit_app.py
```

Then visit `http://localhost:8501`

---

## ✨ Tips

- Keep your app file simple and in the root directory
- Make sure all imports can be resolved
- Use `.gitignore` to exclude large files
- Add comments to your code for clarity
- Consider adding a README.md for documentation

---

## 📞 Support

If you need help:
- Streamlit Docs: https://docs.streamlit.io/
- GitHub Issues: Post in your repository
- Streamlit Community: https://discuss.streamlit.io/

Happy deploying! 🎉
