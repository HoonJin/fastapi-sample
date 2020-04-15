import secrets

from fastapi import HTTPException
from starlette import status

from .domains import UserCreate
from .user_dao import UserDao

from passlib.hash import pbkdf2_sha256


class UserService:
    @staticmethod
    async def sign_up(create: UserCreate) -> int:
        confirm_token = secrets.token_urlsafe(16)
        encrypted_password = pbkdf2_sha256.hash(create.password)
        return await UserDao.insert(create.email, encrypted_password, confirm_token)

    @staticmethod
    async def verify_user(email: str, password: str):
        user = await UserDao.find_by_email(email)
        if user is not None:
            pbkdf2_sha256.verify(password, user.password)
        else:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
