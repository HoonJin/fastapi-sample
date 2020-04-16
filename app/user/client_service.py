import secrets
import string

from fastapi import HTTPException, status

from .client_dao import ClientDao


def generate_random_token(length: int = 32):
    return ''.join([secrets.choice(string.ascii_letters + string.digits) for n in range(length)])


class ClientService:
    @staticmethod
    async def get_client(client_id: str, client_secret: str):
        client = await ClientDao.find_by_client_id(client_id)

        if client is None:
            raise HTTPException(status.HTTP_400_BAD_REQUEST)
        if client.client_secret != client_secret:  # TODO encrypt 또는 hash 사용해야함
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)
        return client

    @staticmethod
    async def create_client(user_id: int, name: str = 'default') -> (str, str):
        client_id = generate_random_token()
        client_secret = generate_random_token(64)
        await ClientDao.insert(user_id, name, client_id, client_secret, '')
        return client_id, client_secret
