from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class Voucher(BaseModel):
    id: int
    name: str
    par_value: Decimal
    category: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]


class VoucherSeller(BaseModel):
    id: int
    name: str
    url: str
    tel: Optional[str]
    address: Optional[str]
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]


class VoucherPrice(BaseModel):
    id: int
    voucher_id: int
    seller_id: int
    side: str
    price: Decimal
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]
