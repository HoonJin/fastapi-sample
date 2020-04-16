from datetime import datetime
from typing import List

from sqlalchemy import Table

from database import db, get_schema
from .domains import Client

clients: Table = get_schema('clients')


class ClientDao:
    @staticmethod
    async def get_by_user_id(user_id: int) -> List[Client]:
        query = clients.select().where(clients.c.user_id == user_id)
        result = await db.fetch_all(query)
        return list(map(lambda x: Client(**x), result))

    @staticmethod
    async def insert(user_id: int, name: str, client_id: str, client_secret: str, scope: str):
        now = datetime.utcnow()
        query = clients.insert().values(user_id=user_id, name=name, client_id=client_id, client_secret=client_secret,
                                        scope=scope, created_at=now, updated_at=now)
        return await db.execute(query)
