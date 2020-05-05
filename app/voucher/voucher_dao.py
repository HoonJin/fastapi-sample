from typing import List

from sqlalchemy import Table

from database import db, get_schema
from .entities import Voucher

vouchers: Table = get_schema('vouchers')


class VoucherDao:
    @staticmethod
    async def get_all() -> List[Voucher]:
        query = vouchers.select()
        return list(map(lambda x: Voucher(**x), await db.fetch_all(query)))
