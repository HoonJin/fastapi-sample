from datetime import datetime
from typing import Optional

from app import AbstractBaseModel
from .domains import UserStatus


class User(AbstractBaseModel):
    uuid: str
    email: str
    encrypted_password: str
    confirmation_token: Optional[str]
    confirmed_at: Optional[datetime]
    status: UserStatus

    class Config:
        orm_mode = True


class Client(AbstractBaseModel):
    user_id: int
    name: str
    client_id: str
    encrypted_secret: str
    scope: str
    trusted: bool
    expires_at: datetime

    class Config:
        orm_mode = True
