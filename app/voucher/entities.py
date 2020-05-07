from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class AbstractBaseModel(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime


class Voucher(AbstractBaseModel):
    uuid: str
    name: str
    par_value: Decimal
    category: str
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True


class VoucherCrawlingSequence(AbstractBaseModel):
    timestamp: int

    class Config:
        orm_mode = True


class VoucherStore(AbstractBaseModel):
    name: str
    url: str
    tel: Optional[str]
    address: Optional[str]
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True


class VoucherPrice(AbstractBaseModel):
    voucher_id: int
    store_id: int
    side: str
    price: Decimal
    sequence_id: int
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True
