from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class UserStatus(str, Enum):
    unconfirmed = 'unconfirmed'
    registered = 'registered'
    dormant = 'dormant'
    terminated = 'terminated'


class User(BaseModel):
    id: int
    email: str
    password: str
    confirmation_token: Optional[str]
    confirmed_at: Optional[datetime]
    status: UserStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: str
    password: str


class Client(BaseModel):
    id: int
    user_id: int
    name: str
    client_id: str
    client_secret: str
    scope: str
    trusted: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
