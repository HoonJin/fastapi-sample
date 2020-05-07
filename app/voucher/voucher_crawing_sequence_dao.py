from datetime import datetime

from sqlalchemy import Table, desc

from database import db, get_schema
from .entities import VoucherCrawlingSequence

voucher_crawling_sequences: Table = get_schema('voucher_crawling_sequences')


class VoucherCrawlingSequenceDao:
    @staticmethod
    async def get_last() -> VoucherCrawlingSequence:
        query = voucher_crawling_sequences.select().order_by(desc(voucher_crawling_sequences.c.created_at))
        return await db.fetch_one(query)

    @staticmethod
    async def insert() -> int:
        now = datetime.utcnow()
        timestamp = int(now.timestamp() * 1000)
        query = voucher_crawling_sequences.insert().values(timestamp=timestamp, created_at=now, updated_at=now)
        return await db.execute(query)
