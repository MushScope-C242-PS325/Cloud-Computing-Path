from pydantic import BaseModel, validator
from typing import Optional
import re

class UserRegister(BaseModel):
    name: str
    email: str
    password: str
    photo_url: Optional[str] = None

    @validator('name')
    def validate_name(cls, v):
        if not v or len(v.strip()) < 2:
            raise ValueError('Name must be at least 2 characters long')
        return v.strip()

    @validator('email')
    def validate_email(cls, v):
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', v):
            raise ValueError('Email format is invalid')
        return v

    @validator('password')
    def validate_password(cls, v):
        if len(v) < 6:
            raise ValueError('Password must be at least 6 characters long')
        return v

class UserLogin(BaseModel):
    email: str
    password: str

    @validator('email')
    def validate_gmail(cls, v):
        if not v.endswith('@gmail.com'):
            raise ValueError('Only gmail.com email addresses are allowed')
        return v

class LoginResult(BaseModel):
    userId: str
    name: str
    token: str
    photo_url: Optional[str] = None

class ErrorResponse(BaseModel):
    error: bool
    message: str

class LoginSuccessResponse(BaseModel):
    error: bool
    message: str
    loginResult: LoginResult

class LoginFailureResponse(BaseModel):
    error: bool = True
    message: str
    status_code: int = 401

class ProfileResponse(BaseModel):
    error: bool = False
    message: str
    detail: dict
