import secrets
import string

import jwt
from fastapi.security import OAuth2PasswordRequestForm
from jwt import InvalidTokenError

from config.exceptions import BadRequestException, UnauthorizedException
from .client_dao import ClientDao
from .domains import User, TokenResponse
from .user_dao import UserDao
from .user_service import UserService

user_service = UserService()
_ALGORITHM = 'HS256'


def generate_random_token(length: int = 32):
    return ''.join([secrets.choice(string.ascii_letters + string.digits) for n in range(length)])


class ClientService:
    @staticmethod
    async def get_client(client_id: str, client_secret: str):
        client = await ClientDao.find_by_client_id(client_id)

        if client is None:
            raise BadRequestException
        if client.client_secret != client_secret:  # TODO encrypt 또는 hash 사용해야함
            raise UnauthorizedException
        return client

    @staticmethod
    async def create_client(user: User, name: str = 'default') -> (str, str):
        client_id = generate_random_token()
        client_secret = generate_random_token(64)
        await ClientDao.insert(user.id, name, client_id, client_secret, '')
        return client_id, client_secret

    @staticmethod
    async def create_access_token(form: OAuth2PasswordRequestForm) -> TokenResponse:
        user = await user_service.authenticate_user(form.username, form.password)
        client = await ClientDao.find_by_client_id(form.client_id)
        if client is not None and client.client_secret == form.client_secret:
            data = {'uuid': user.uuid, 'client_id': client.client_id}
            access_token = jwt.encode(data, client.client_secret).decode()
            return TokenResponse(access_token=access_token)
        else:
            raise UnauthorizedException

    @staticmethod
    async def get_user_by_access_token(access_token: str):
        if access_token is None:
            raise BadRequestException
        unverified_data = jwt.decode(access_token, verify=False, algorithms=[_ALGORITHM])
        client = await ClientDao.find_by_client_id(unverified_data.get('client_id'))
        secret = client.client_secret
        try:
            data = jwt.decode(access_token, secret, algorithms=[_ALGORITHM])
            user_uuid = data.get('uuid')
            user = await UserDao.find_by_uuid(user_uuid)
            if user is None:
                raise BadRequestException
            return user
        except InvalidTokenError as e:
            raise UnauthorizedException(str(e))
