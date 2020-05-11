from datetime import datetime
from typing import List, Optional

from sqlalchemy import Table

from database import db, get_schema
from .entities import Client

clients: Table = get_schema('clients')


class ClientDao:
    @staticmethod
    async def get_by_user_id(user_id: int) -> List[Client]:
        query = clients.select().where(clients.c.user_id == user_id)
        result = await db.fetch_all(query)
        return list(map(lambda x: Client(**x), result))

    @staticmethod
    async def find_by_client_id(client_id: str) -> Optional[Client]:
        query = clients.select().where(clients.c.client_id == client_id)
        result = await db.fetch_one(query)
        return Client(**result) if result is not None else None

    @staticmethod
    async def update_expires_at(client_id: str, expires_at: datetime):
        query = clients.update().where(clients.c.client_id == client_id)\
            .values(expires_at=expires_at, updated_at=datetime.utcnow())
        return await db.execute(query)

    @staticmethod
    async def insert(user_id: int, name: str, client_id: str, encrypted_secret: str, scope: str = ''):
        now = datetime.utcnow()
        query = clients.insert()\
            .values(user_id=user_id, name=name, client_id=client_id, encrypted_secret=encrypted_secret, scope=scope,
                    expires_at=now, created_at=now, updated_at=now)
        return await db.execute(query)
