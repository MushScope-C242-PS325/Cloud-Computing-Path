# Authentication API Using FastAPI & Firebase 



## ⚡️ Why This Stack?
- **FastAPI**: Blazing fast performance with async support
- **Firebase**: Production-ready authentication and storage
- **Python 3.8+**: Modern Python features and type hints
- **Swagger/ReDoc**: Auto-generated API documentation




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

```


## 🔒 Security Best Practices
- Use HTTPS in production
- Implement rate limiting
- Keep `.env` and `serviceKey.json` secure
- Regular dependency updates
- Input validation using Pydantic models
- Proper error handling


## 🤝 Contributing
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a Pull Request
