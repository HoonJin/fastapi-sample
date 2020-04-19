import secrets

from passlib.hash import pbkdf2_sha256

from config.exceptions import UnauthorizedException, NotFoundException
from .domains import UserCreate
from .entities import User
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
            if pbkdf2_sha256.verify(password, user.encrypted_password):
                return user
            else:
                raise UnauthorizedException
        else:
            raise NotFoundException
