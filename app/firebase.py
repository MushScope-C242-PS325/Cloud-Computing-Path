import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

def initialize_firebase():
    try:

        base_dir = Path(__file__).resolve().parent
        service_path = base_dir / "services" / "serviceKey.json"

        if not service_path.exists():
            raise FileNotFoundError(f"Service account file not found at: {service_path}")

        if not firebase_admin._apps:
            cred = credentials.Certificate(str(service_path))
            firebase_admin.initialize_app(cred)

        return firestore.client()
    
    except Exception as e:
        raise Exception(f"Failed to initialize Firebase: {str(e)}")

try:
    db = initialize_firebase()
except Exception as e:
    print(f"Error initializing Firebase: {e}")
    raise

def get_firestore_client():
    """Returns the Firestore client instance"""
    return db