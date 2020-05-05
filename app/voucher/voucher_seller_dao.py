from typing import List, Optional

from sqlalchemy import Table

from database import db, get_schema
from .entities import VoucherSeller

voucher_sellers: Table = get_schema('voucher_sellers')


class VoucherSellerDao:
    @staticmethod
    async def get_all() -> List[VoucherSeller]:
        query = voucher_sellers.select()
        return list(map(lambda x: VoucherSeller(**x), await db.fetch_all(query)))

    @staticmethod
    async def find_by_id(seller_id: int) -> Optional[VoucherSeller]:
        query = voucher_sellers.select().where(voucher_sellers.c.id == seller_id)
        result = await db.fetch_one(query)
        return VoucherSeller(**result) if result is not None else None
