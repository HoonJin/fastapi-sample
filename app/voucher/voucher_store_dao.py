from typing import List, Optional

from sqlalchemy import Table

from database import db, get_schema
from .entities import VoucherStore

voucher_stores: Table = get_schema('voucher_stores')


class VoucherStoreDao:
    @staticmethod
    async def get_all() -> List[VoucherStore]:
        query = voucher_stores.select()
        return list(map(lambda x: VoucherStore(**x), await db.fetch_all(query)))

    @staticmethod
    async def find_by_id(store_id: int) -> Optional[VoucherStore]:
        query = voucher_stores.select().where(voucher_stores.c.id == store_id)
        result = await db.fetch_one(query)
        return VoucherStore(**result) if result is not None else None
