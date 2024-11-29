from fastapi import FastAPI
from app.auth import router as auth_router
from app.firebase import FirebaseInit

db = FirebaseInit.get_firestore()

app = FastAPI(
    title="Authentication API",
    description="API for user authentication"
)

app.include_router(auth_router)
