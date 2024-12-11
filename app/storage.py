from firebase_admin import storage
from fastapi import UploadFile
from typing import Optional
from .firebase import FirebaseInit
import logging
import os
import uuid

logger = logging.getLogger(__name__)

class StorageService:
    def __init__(self):
        self.bucket = FirebaseInit.get_storage()
        
    async def upload_file(self, file: UploadFile, path: str) -> Optional[str]:
        try:
            content = await file.read()
            if len(content) > 1_048_576: 
                raise ValueError("The photo size must be less than 1MB")

            file_ext = os.path.splitext(file.filename)[1].lower()
            if file_ext not in ['.jpg', '.png']:
                raise ValueError("Only .jpg and .png files are allowed")

            blob = self.bucket.blob(path)
            blob.upload_from_string(content, content_type=file.content_type)
            blob.make_public()

            logger.info(f"File uploaded successfully to {path}")
            return blob.public_url
            
        except Exception as e:
            logger.error(f"Error uploading file: {str(e)}")
            raise
