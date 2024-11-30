# Firebase Authentication Service

A Python-based authentication service utilizing Firebase for secure user management and authentication.


## 🚀 Features
- Firebase Authentication integration
- Secure user management
- File storage capabilities
- Schema validation
- Environment configuration

## 🔧 Prerequisites
- Python 3.8 or higher
- Firebase project credentials
- pip (Python package installer)

## 🛠️ Installation & Setup

1. **Create and Activate Virtual Environment**

   **For Windows:**
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate virtual environment
   venv\Scripts\activate
   ```

   **For Linux/MacOS:**
   ```bash
   # Create virtual environment
   python3 -m venv venv

   # Activate virtual environment
   source venv/bin/activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**
   
   Create a `.env` file in the root directory with the following variables:
   ```env
   FIREBASE_API_KEY=your_api_key
   FIREBASE_AUTH_DOMAIN=your_auth_domain
   FIREBASE_PROJECT_ID=your_project_id
   FIREBASE_STORAGE_BUCKET=your_storage_bucket
   FIREBASE_SERVICE_ACCOUNT_PATH=service/serviceKey.json
   ```

4. **Firebase Service Account**
   
   Place your Firebase `serviceKey.json` in the `service/` directory.

## 🏃‍♂️ Running the Application

1. Ensure your virtual environment is activated
2. Run the main application:
   ```bash
   python main.py
   ```

## 📚 API Documentation

### Authentication Endpoints
- `/auth/register` - Register new user
- `/auth/login` - User login
- `/auth/logout` - User logout

### Storage Operations
- File upload/download functionality
- Secure file storage management

## 🔒 Security Notes
- Keep your `.env` and `serviceKey.json` files secure and never commit them to version control
- Implement proper authentication checks
- Regular security updates and monitoring

## 🤝 Contributing
1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## 📝 License
This project is licensed under the MIT License - see the LICENSE file for details
