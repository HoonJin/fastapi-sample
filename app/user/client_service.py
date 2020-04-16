import secrets
import string

from .client_dao import ClientDao


class ClientService:
    @staticmethod
    def generate_random_token(length: int = 32):
        return ''.join([secrets.choice(string.ascii_letters + string.digits) for n in range(length)])

    @staticmethod
    async def create_client(user_id: int, name: str = 'default') -> (str, str):
        client_id = ClientService.generate_random_token()
        client_secret = ClientService.generate_random_token(64)
        await ClientDao.insert(user_id, name, client_id, client_secret, '')
        return client_id, client_secret
