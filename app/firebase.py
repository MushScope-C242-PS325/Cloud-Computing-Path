from firebase_admin import credentials, firestore, storage
from pathlib import Path
import os
import firebase_admin

class FirebaseInit:
    _instance = None
    _initialized = False
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def __init__(self):
        if not FirebaseInit._initialized:
            try:
                cred_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS', 'service/serviceKey.json')
                
                if not os.path.exists(cred_path):
                    raise FileNotFoundError(
                        f"Firebase service account key not found at {cred_path}"
                    )
                    
                cred = credentials.Certificate(cred_path)
                firebase_admin.initialize_app(cred, {
                    'storageBucket': os.getenv('FIREBASE_STORAGE_BUCKET')
                })
                FirebaseInit._initialized = True
            except Exception as e:
                print(f"Firebase initialization error: {str(e)}")
                raise

    @staticmethod
    def get_firestore():
        return firestore.client()

    @staticmethod
    def get_storage():
        return storage.bucket()

firebase_init = FirebaseInit()

__all__ = ['FirebaseInit', 'firebase_init']
