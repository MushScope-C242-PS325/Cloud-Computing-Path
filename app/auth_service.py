from firebase_admin import auth
from fastapi import HTTPException, status
from schemas import UserRegister, UserLogin, LoginResult, ErrorResponse, LoginSuccessResponse

class AuthService:
    @staticmethod
    async def register_user(user: UserRegister) -> ErrorResponse:
        try:
            try:
                existing_user = auth.get_user_by_email(user.email)
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail={
                        "error": True,
                        "message": "Email already registered"
                    }
                )
            except auth.UserNotFoundError:
                pass

            user_record = auth.create_user(
                email=user.email,
                password=user.password,
                display_name=user.name
            )

            return ErrorResponse(
                error=False,
                message="User Created"
            )

        except Exception as e:
            if isinstance(e, HTTPException):
                raise e
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail={
                    "error": True,
                    "message": str(e)
                }
            )

    @staticmethod
    async def login_user(user: UserLogin) -> LoginSuccessResponse:
        try:
            user_record = auth.get_user_by_email(user.email)
            
            custom_token = auth.create_custom_token(user_record.uid)
            
            login_result = LoginResult(
                userId=f"user-{user_record.uid[:10]}",
                name=user_record.display_name,
                token=custom_token.decode()
            )

            return LoginSuccessResponse(
                error=False,
                message="success",
                loginResult=login_result
            )

        except auth.UserNotFoundError:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "error": True,
                    "message": "User not found"
                }
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail={
                    "error": True,
                    "message": str(e)
                }
            )