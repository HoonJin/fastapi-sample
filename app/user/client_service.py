from config.exceptions import BadRequestException, UnauthorizedException, ErrorCode
from app.utils import secret_util, string_util
from .client_dao import ClientDao
from .entities import User, Client


class ClientService:
    @staticmethod
    async def create_client(user: User, name: str = 'default') -> (str, str):
        client_id = string_util.generate_random_token()
        client_secret = string_util.generate_random_token()
        encrypted = secret_util.encrypt(client_secret)
        await ClientDao.insert(user.id, name, client_id, encrypted)
        return client_id, client_secret

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
