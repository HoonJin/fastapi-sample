import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import Table, and_

from database import db, get_schema
from .entities import User

users: Table = get_schema('users')


class UserDao:
    @staticmethod
    async def get_by_id(user_id: int) -> User:
        query = users.select().where(users.c.id == user_id)
        return User(**await db.fetch_one(query))

    @staticmethod
    async def find_by_uuid(uid: str) -> Optional[User]:
        query = users.select().where(users.c.uuid == uid)
        result = await db.fetch_one(query)
        return User(**result) if result is not None else None

    @staticmethod
    async def find_by_email_and_confirmed_at_is_not_null(email: str) -> Optional[User]:
        query = users.select().where(and_(users.c.email == email, users.c.confirmed_at != None))
        result = await db.fetch_one(query)
        return User(**result) if result is not None else None

    @staticmethod
    async def insert(email: str, encrypted_password: str, confirmation_token: str):
        now = datetime.utcnow()
        query = users.insert().values(email=email, uuid=str(uuid.uuid4()), encrypted_password=encrypted_password,
                                      confirmation_token=confirmation_token, created_at=now, updated_at=now)
        return await db.execute(query)
