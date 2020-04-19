import secrets
import string
from datetime import datetime, timedelta

import jwt
from cryptography.fernet import Fernet
from jwt import InvalidTokenError

import config
from config.exceptions import BadRequestException, UnauthorizedException, ErrorCode
from .client_dao import ClientDao
from .domains import TokenResponse, LoginForm, ClientForm
from .entities import User
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
            data = {'uuid': user.uuid, 'client_id': client.client_id, 'expires_at': renew_time.timestamp()}
            access_token = jwt.encode(data, form.client_secret).decode()
            return TokenResponse(access_token=access_token)
        else:
            raise UnauthorizedException

    @staticmethod
    async def login(form: LoginForm) -> TokenResponse:
        user = await user_service.authenticate_user(form.username, form.password)
        if user is None:
            raise UnauthorizedException

        expires_at = (datetime.utcnow() + timedelta(days=1)).timestamp()
        data = {'uuid': user.uuid, 'service': form.service, 'expires_at': expires_at}
        access_token = jwt.encode(data, login_secret).decode()
        return TokenResponse(access_token=access_token)

    @staticmethod
    async def get_user_by_access_token(access_token: str):
        if access_token is None:
            raise BadRequestException
        unverified_data = jwt.decode(access_token, verify=False, algorithms=[_ALGORITHM])
        client_id = unverified_data.get('client_id')

        try:
            if client_id is None:  # 일반적인 로그인 경우
                service = unverified_data.get('service')
                if service is None:
                    raise UnauthorizedException
                data = jwt.decode(access_token, login_secret, algorithms=[_ALGORITHM])
            else:  # access_token 사용 경우
                client = await ClientDao.find_by_client_id(client_id)
                if not client.trusted:
                    raise UnauthorizedException('신뢰할 수 없는 키')
                secret = decrypt(client.encrypted_secret)
                data = jwt.decode(access_token, secret, algorithms=[_ALGORITHM])
        except InvalidTokenError as e:  # jwt 토큰 검증에 실패한 경우
            raise UnauthorizedException(str(e))

        if data.get('expires_at') < datetime.utcnow().timestamp():
            raise BadRequestException(ErrorCode.token_expired)

        user_uuid = data.get('uuid')
        user = await UserDao.find_by_uuid(user_uuid)
        if user is None:
            raise BadRequestException
        return user
