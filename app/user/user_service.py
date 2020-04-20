import secrets

from passlib.hash import pbkdf2_sha256

from config.exceptions import UnauthorizedException, NotFoundException
from .domains import UserStatus
from .entities import User
from .user_dao import UserDao


class UserService:
    @staticmethod
    async def sign_up(email: str, password: str) -> int:
        confirm_token = secrets.token_urlsafe(16)
        encrypted_password = pbkdf2_sha256.hash(password)
        return await UserDao.insert(email, encrypted_password, confirm_token)

    @staticmethod
    async def authenticate_user(email: str, password: str) -> User:
        user = await UserDao.find_by_email(email)
        if user is None:
            raise NotFoundException
        if user.confirmed_at is None and user.status != UserStatus.registered:
            raise UnauthorizedException(detail='confirmation is required')
        if not pbkdf2_sha256.verify(password, user.encrypted_password):
            raise UnauthorizedException(detail='password is wrong')
        return user

    @staticmethod
    async def confirm(token: str):
        user = await UserDao.find_by_confirmation_token(token)
        if user is None:
            raise NotFoundException
        return await UserDao.update_confirmed(user.id)
