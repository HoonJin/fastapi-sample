from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Test(BaseModel):
    id: int
    varchar: Optional[str]
    created: datetime

    class Config:
        orm_mode = True


class TestCreate(BaseModel):
    varchar: str
