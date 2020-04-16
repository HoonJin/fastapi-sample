import secrets

from fastapi import HTTPException
from passlib.hash import pbkdf2_sha256
from starlette import status

from .domains import UserCreate, User
from .user_dao import UserDao


class UserService:
    @staticmethod
    async def sign_up(create: UserCreate) -> int:
        confirm_token = secrets.token_urlsafe(16)
        encrypted_password = pbkdf2_sha256.hash(create.password)
        return await UserDao.insert(create.email, encrypted_password, confirm_token)

    @staticmethod
    async def authenticate_user(email: str, password: str) -> User:
        user = await UserDao.find_by_email_and_confirmed_at_is_not_null(email)
        if user is not None:
            if pbkdf2_sha256.verify(password, user.password):
                return user
            else:
                raise HTTPException(status.HTTP_401_UNAUTHORIZED)
        else:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
