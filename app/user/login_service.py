import logging
from datetime import datetime, timedelta

import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from config.exceptions import UnauthorizedException, BadRequestException, ErrorCode
from app.utils import secret_util
from .client_dao import ClientDao
from .client_service import ClientService
from .domains import ClientForm, TokenResponse, LoginForm
from .entities import User
from .user_dao import UserDao
from .user_service import UserService

_ALGORITHM = 'HS256'
login_secret = 'asdfjsdkvnkjqwnvqwi23hur2funnviwenvw'


class LoginService:
    @staticmethod
    async def create_access_token(form: ClientForm) -> TokenResponse:
        client = await ClientDao.find_by_client_id(form.client_id)
        if not client.trusted:
            raise UnauthorizedException(detail='신뢰할 수 없는 키')

        if client is not None and secret_util.decrypt(client.encrypted_secret) == form.client_secret:
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
        user = await UserService.authenticate_user(form.username, form.password)

        expires_at = (datetime.utcnow() + timedelta(days=1)).timestamp()
        payload = {'uuid': user.uuid, 'iss': form.service, 'exp': expires_at}
        access_token = jwt.encode(payload, login_secret).decode()
        return TokenResponse(access_token=access_token)

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
                secret = secret_util.decrypt(client.encrypted_secret)
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


__oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


async def get_current_user(token: str = Depends(__oauth2_scheme)) -> User:
    return await LoginService.get_user_by_access_token(token)
