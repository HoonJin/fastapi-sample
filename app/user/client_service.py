import logging
import secrets
import string
from datetime import datetime, timedelta

import jwt
from cryptography.fernet import Fernet

import config
from config.exceptions import BadRequestException, UnauthorizedException, ErrorCode
from .client_dao import ClientDao
from .domains import TokenResponse, LoginForm, ClientForm
from .entities import User, Client
from .user_dao import UserDao
from .user_service import UserService

user_service = UserService()
fernet = Fernet(config.SECRET_KEY)
_ALGORITHM = 'HS256'

login_secret = 'asdfjsdkvnkjqwnvqwi23hur2funnviwenvw'


def encrypt(plain_str: str) -> str:
    return fernet.encrypt(plain_str.encode()).decode()


def decrypt(encrypted: str) -> str:
    return fernet.decrypt(encrypted.encode()).decode()


def generate_random_token(length: int = 32):
    return ''.join([secrets.choice(string.ascii_letters + string.digits) for n in range(length)])


class ClientService:
    @staticmethod
    async def create_client(user: User, name: str = 'default') -> (str, str):
        client_id = generate_random_token()
        client_secret = generate_random_token()
        encrypted = encrypt(client_secret)
        await ClientDao.insert(user.id, name, client_id, encrypted)
        return client_id, client_secret

    @staticmethod
    async def create_access_token(form: ClientForm) -> TokenResponse:
        client = await ClientDao.find_by_client_id(form.client_id)
        if not client.trusted:
            raise UnauthorizedException(detail='신뢰할 수 없는 키')

        if client is not None and decrypt(client.encrypted_secret) == form.client_secret:
            user = await UserDao.get_by_id(client.user_id)
            renew_time = datetime.utcnow() + timedelta(days=1)
            await ClientDao.update_expires_at(form.client_id, renew_time)
            payload = {'uuid': user.uuid, 'client_id': client.client_id, 'exp': renew_time.timestamp()}
            access_token = jwt.encode(payload, form.client_secret).decode()
            return TokenResponse(access_token=access_token)
        else:
            raise UnauthorizedException

    @staticmethod
    async def login(form: LoginForm) -> TokenResponse:
        user = await user_service.authenticate_user(form.username, form.password)
        if user is None:
            raise UnauthorizedException

        expires_at = (datetime.utcnow() + timedelta(days=1)).timestamp()
        payload = {'uuid': user.uuid, 'iss': form.service, 'exp': expires_at}
        access_token = jwt.encode(payload, login_secret).decode()
        return TokenResponse(access_token=access_token)

    @staticmethod
    async def get_validated_client(client_id: str) -> Client:
        if client_id is None:
            raise BadRequestException
        client = await ClientDao.find_by_client_id(client_id)
        if client is None:
            raise BadRequestException(ErrorCode.invalid_client)
        if not client.trusted:
            raise UnauthorizedException(detail='신뢰할 수 없는 키')
        return client

    @staticmethod
    async def get_user_by_access_token(access_token: str):
        # exp 의 경우 utc 로 설정했는데 인증할 때 kst 현재시간을 기준으로 처리해서 처리가 되지 않음
        # 따라서 수동으로 처리
        verify_options = {'verify_exp': False}
        if access_token is None:
            raise BadRequestException
        data = jwt.decode(access_token, verify=False, algorithms=[_ALGORITHM])

        try:
            issuer = data.get('iss')
            if issuer is not None:
                # TODO issuer 로 secret 키를 맵핑시켜서 decode 할 것
                payload = jwt.decode(access_token, login_secret, algorithms=[_ALGORITHM], options=verify_options)
            else:  # access_token 사용 경우
                client = await ClientService.get_validated_client(data.get('client_id'))
                secret = decrypt(client.encrypted_secret)
                payload = jwt.decode(access_token, secret, algorithms=[_ALGORITHM], options=verify_options)
        except jwt.InvalidTokenError as e:  # jwt 토큰 검증에 실패한 경우
            logging.error(e, exc_info=True)
            raise UnauthorizedException(detail=str(e))

        if payload.get('exp') < datetime.utcnow().timestamp():
            raise BadRequestException(ErrorCode.token_expired)

        user = await UserDao.find_by_uuid(payload.get('uuid'))
        if user is None:
            raise BadRequestException
        return user
