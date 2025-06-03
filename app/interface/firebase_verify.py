import firebase_admin
from firebase_admin import credentials, auth
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize Firebase Admin SDK (do this once at startup)
if not firebase_admin._apps:
    service_account_path = os.getenv("FIREBASE_SERVICE_ACCOUNT")
    cred = credentials.Certificate(service_account_path)
    firebase_admin.initialize_app(cred)

def verify_firebase_token(id_token):
    """
    Verifies a Firebase ID token (from Google, Yahoo, Facebook, Phone, etc.)
    Returns decoded user info if valid, else None.
    """
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token  # Contains uid, email, etc.
    except Exception as e:
        print("Token verification failed:", e)
        return None

# Example usage (for testing):
if __name__ == "__main__":
    token = input("Paste Firebase ID token here: ")
    user_info = verify_firebase_token(token)
    if user_info:
        print("User is authenticated:", user_info)
    else:
        print("Invalid token")