# 🌩️ Cloudrive – Secure Cloud File Storage with Firebase Auth & Google Cloud Storage

Cloudrive is a web-based file storage system that allows users to securely upload, view, download, and delete personal files using their authenticated Firebase account. It leverages Firebase Authentication for secure login and Google Cloud Storage (GCS) for reliable and scalable file storage.

---

## 🚀 Features

- 🔐 User authentication with Firebase (JWT-based)
- ☁️ Upload, list, download, and delete user files
- 📁 Google Cloud Storage backend
- 🌐 Hosted using Render with secret environment variables
- 🔄 Clean, per-user file access control
- 🧪 CORS-enabled API for frontend/backend communication
- ✅ Minimal and intuitive HTML frontend

---

## 🛠️ Technologies Used

- Python 3 (Flask)
- Firebase Admin SDK
- Google Cloud Storage (Python Client)
- Flask-CORS
- dotenv (.env for secure local testing)
- Render (for deployment)

---

## 📁 Project Structure

cloudrive/
│
├── app.py # Flask backend
├── requirements.txt # Python dependencies
├── .gitignore
├── .env # Environment variables
├── firebase-key.json # Decoded at runtime
├── gcs-key.json # Decoded at runtime
├── templates/
│ └── index.html # HTML frontend
└── static/
└── favicon.png # Tab icon

---

## 🌐 Live Demo

= Deployed using Render:  
  https://cloudrora.onrender.com

---

## 🔑 Environment Variables

Create a `.env` file in the root of your project:

```env
FIREBASE_CREDENTIALS_BASE64=your_base64_encoded_firebase_key
GOOGLE_CREDENTIALS_BASE64=your_base64_encoded_gcs_key
```

## 📸 Screenshots


