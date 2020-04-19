from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from .domains import UserStatus


class User(BaseModel):
    id: int
    uuid: str
    email: str
    encrypted_password: str
    confirmation_token: Optional[str]
    confirmed_at: Optional[datetime]
    status: UserStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class Client(BaseModel):
    id: int
    user_id: int
    name: str
    client_id: str
    encrypted_secret: str
    scope: str
    trusted: bool
    expires_at: datetime
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
