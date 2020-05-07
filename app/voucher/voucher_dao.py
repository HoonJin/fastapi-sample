from typing import List, Optional

from sqlalchemy import Table

from database import db, get_schema
from .entities import Voucher

vouchers: Table = get_schema('vouchers')


class VoucherDao:
    @staticmethod
    async def get_all() -> List[Voucher]:
        query = vouchers.select()
        return list(map(lambda x: Voucher(**x), await db.fetch_all(query)))

    @staticmethod
    async def find_by_uuid(uid: str) -> Optional[Voucher]:
        query = vouchers.select().where(vouchers.c.uuid == uid)
        result = await db.fetch_one(query)
        return Voucher(**result) if result is not None else None
