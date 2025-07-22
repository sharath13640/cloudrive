from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from google.cloud import storage
import firebase_admin
from firebase_admin import credentials, auth
import os
from datetime import timedelta
import os
import base64
import json
from dotenv import load_dotenv

# Optional: load .env locally
load_dotenv()

# Decode and write Firebase credentials
firebase_b64 = os.environ.get("FIREBASE_CREDENTIALS_BASE64")
if firebase_b64:
    with open("firebase-key.json", "wb") as f:
        f.write(base64.b64decode(firebase_b64))
else:
    raise RuntimeError("Missing FIREBASE_CREDENTIALS_BASE64 env var")

# Decode and write GCS credentials
gcs_b64 = os.environ.get("GOOGLE_CREDENTIALS_BASE64")
if gcs_b64:
    with open("gcs-key.json", "wb") as f:
        f.write(base64.b64decode(gcs_b64))
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcs-key.json"
else:
    raise RuntimeError("Missing GOOGLE_CREDENTIALS_BASE64 env var")


app = Flask(__name__)
CORS(app)

# Initialize Firebase Admin SDK
firebase_cred = credentials.Certificate("firebase-key.json")  # Your Firebase Admin SDK file
firebase_admin.initialize_app(firebase_cred)

# Set Google Cloud credentials (GCS key)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcs-key.json"  # Your GCS key file
BUCKET_NAME = "my-cloud-drive-bucket"  # Change to your actual GCS bucket name
client = storage.Client()
bucket = client.bucket(BUCKET_NAME)

# Helper to verify Firebase ID token
def verify_token(request):
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        return None
    id_token = auth_header.split(" ")[1]
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token.get("email")
    except Exception as e:
        print("Token verification error:", e)
        return None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    email = verify_token(request)
    if not email:
        return "Unauthorized", 401
    try:
        file = request.files["file"]
        blob = bucket.blob(f"{email}/{file.filename}")
        blob.upload_from_file(file)
        return "Uploaded successfully"
    except Exception as e:
        return str(e), 500

@app.route("/list", methods=["GET"])
def list_files():
    email = verify_token(request)
    if not email:
        return "Unauthorized", 401
    try:
        blobs = bucket.list_blobs(prefix=f"{email}/")
        filenames = [blob.name.replace(f"{email}/", "", 1) for blob in blobs]
        return jsonify(filenames)
    except Exception as e:
        return str(e), 500

@app.route("/download/<filename>", methods=["GET"])
def download(filename):
    email = verify_token(request)
    if not email:
        return "Unauthorized", 401
    try:
        blob = bucket.blob(f"{email}/{filename}")
        if not blob.exists():
            return "File not found", 404
        signed_url = blob.generate_signed_url(
            version="v4",
            expiration=timedelta(minutes=10),
            method="GET"
        )
        return jsonify({"url": signed_url})
    except Exception as e:
        return str(e), 500

@app.route("/delete/<filename>", methods=["DELETE"])
def delete(filename):
    email = verify_token(request)
    if not email:
        return "Unauthorized", 401
    try:
        blob = bucket.blob(f"{email}/{filename}")
        blob.delete()
        return f"{filename} deleted successfully"
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(debug=True)
