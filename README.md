# Authentication API Using FastAPI & Firebase 

## 🛠️ Technologies Used
- **FastAPI**: High-performance Python web framework for building APIs
- **Visual Studio Code (VSCode)**: Integrated Development Environment (IDE) for development
- **Python**: Primary programming language
- **Postman**: API testing tool
- **Firebase**: Authentication and storage service

## 📝 Project Purpose
This project aims to build an authentication API server that enables:
- New user registration
- User login process
- Retrieving user profile information
- Secure authentication using tokens

## 🛠️ Installation & Setup
1. **Create and Activate Virtual Environment**
   **For Windows:**
   ```bash
   # Create virtual environment
   python -m venv your_venv_name
   # Activate virtual environment
   venv\Scripts\activate
   ```
   **For Linux/MacOS:**
   ```bash
   # Create virtual environment
   python3 -m venv your_venv_name
   # Activate virtual environment
   source venv/bin/activate
   ```
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure Environment Variables**
   
   Create a `.env` file in the root directory:
   ```env
   # Firebase Configuration
   
   # FastAPI Configuration
   ```
4. **Firebase Service Account**
   
   Place your Firebase `serviceKey.json` in the `service/` directory.

## 🏃‍♂️ Running the Application
1. **Development Server**
   ```bash
   # Run with default settings
   uvicorn main:app --reload
   # Run with custom host and port
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```
2. **Production Server**
   ```bash
   # Run without reload
   uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
   ```

## 📚 API Documentation
Once the server is running, access the interactive API documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Authentication Endpoints
```python
Method
POST
http://localhost:8000/register
- Register new user
- Body: {
    "name": "User Name"
    "email": "user@example.com",
    "password": "securepassword"    
}

Method
POST
http://localhost:8000/login
- User login
- Body: {
    "email": "user@example.com",
    "password": "securepassword"
}

Method
GET
http://localhost:8000/userProfile
- User Profile
- Authorization: Bearer <your_token>
```

## 🔒 Security Best Practices
- Use HTTPS in production
- Implement rate limiting
- Keep `.env` and `serviceKey.json` secure
- Regular dependency updates
- Input validation using Pydantic models
- Proper error handling
