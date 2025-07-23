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

---![WhatsApp Image 2025-07-23 at 12 24 35_3621594b](https://github.com/user-attachments/assets/7d93b45c-7800-4962-a7b1-96d6054689f8)


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

<img width="1920" height="1080" alt="Screenshot (136)" src="https://github.com/user-attachments/assets/860b4e95-f4f9-410d-92ad-928fa13aa05f" />
<img width="1920" height="1080" alt="Screenshot (137)" src="https://github.com/user-attachments/assets/3a857f81-7d73-4e53-bea2-fd1cce83df07" />
<img width="1920" height="1080" alt="Screenshot (139)" src="https://github.com/user-attachments/assets/16f5b849-6d01-4f11-a653-dea2966a279c" />
<img width="1920" height="1080" alt="Screenshot (141)" src="https://github.com/user-attachments/assets/d14abbd8-e2da-4ea4-a774-2232819c494d" />
<img width="1920" height="1080" alt="Screenshot (142)" src="https://github.com/user-attachments/assets/8078cae0-309e-4cc7-b78d-70f16b6329e4" />

![WhatsApp Image 2025-07-23 at 12 24 35_44359830](https://github.com/user-attachments/assets/d348ba40-686a-4ccc-a2cb-8fc34afdbaaa)
![WhatsApp Image 2025-07-23 at 12 24 57_89d465ac](https://github.com/user-attachments/assets/e9129645-f97c-4f95-af7b-bbd5b19cc838)
