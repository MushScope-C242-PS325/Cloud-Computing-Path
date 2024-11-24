from fastapi import FastAPI
from firebase import get_firestore_client
from auth import router as auth_router

db = get_firestore_client()

app = FastAPI(
    title="Authentication API",
    description="API for user authentication"
)

app.include_router(auth_router)