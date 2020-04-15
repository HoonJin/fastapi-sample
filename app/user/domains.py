from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: int
    email: str
    password: str
    confirm_token: Optional[str]
    confirmed_at: Optional[datetime]
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: str
    password: str
