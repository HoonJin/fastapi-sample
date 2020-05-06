from datetime import datetime
from decimal import Decimal
from typing import List

from sqlalchemy import Table

from database import db, get_schema
from .entities import VoucherPrice

voucher_prices: Table = get_schema('voucher_prices')


class VoucherPriceDao:
    @staticmethod
    async def get_by_voucher_id(voucher_id: int) -> List[VoucherPrice]:
        query = voucher_prices.select().where(voucher_prices.c.voucher_id == voucher_id)
        return list(map(lambda x: VoucherPrice(**x), await db.fetch_all(query)))

    @staticmethod
    async def insert(voucher_id: int, store_id: int, side: str, price: Decimal, sequence_id: int = 0):
        now = datetime.utcnow()
        query = voucher_prices.insert().values(voucher_id=voucher_id, store_id=store_id, side=side, price=price,
                                               sequence_id=sequence_id, created_at=now, updated_at=now)
        return await db.execute(query)
