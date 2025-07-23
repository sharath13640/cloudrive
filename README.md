# ☁️ My CloudDrive – Personalized Cloud Storage

My CloudDrive is a simple yet powerful web-based personal cloud storage system inspired by Google Drive. It allows users to upload, download, delete, and list files securely using Google Cloud Storage. The project is built using Python (Flask) for the backend and HTML/CSS/JavaScript for the frontend.

## ✅ Features

- 📤 Upload files to cloud
- 📥 Download stored files
- ❌ Delete files from cloud
- 📝 List all uploaded files
- 🌐 Google Cloud Storage integration
- 🔐 Secure backend authentication using Service Account
- 🎨 Aesthetic UI with file-type icons and day/night theme toggle
- 🕒 Auto-delete files after 7 days via GCS lifecycle rules

## 🛠️ Technologies Used

- Python (Flask)
- HTML5 / CSS3 / JavaScript
- Google Cloud Storage (GCS)
- Render (for backend deployment)

## 🌐 Live Demo

= Deployed using Render:  
  https://cloud-drive-t1vs.onrender.com


## 🚀 Deployment

Backend: Deployed on Render using Gunicorn

Added GOOGLE_APPLICATION_CREDENTIALS as a secret file

Frontend: Can be deployed on Netlify, GitHub Pages, or Render static site

## 🧹 Auto File Cleanup

The GCS bucket has a lifecycle rule that deletes files automatically after 7 days to manage storage efficiently.

## 📸 Screenshots


