from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class AbstractBaseModel(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime


class Voucher(AbstractBaseModel):
    name: str
    par_value: Decimal
    category: str
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True


class VoucherSeller(AbstractBaseModel):
    name: str
    url: str
    tel: Optional[str]
    address: Optional[str]
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True


class VoucherPrice(AbstractBaseModel):
    voucher_id: int
    seller_id: int
    side: str
    price: Decimal
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True
