from datetime import datetime

from sqlalchemy import Table, desc

from database import db, get_schema
from .entities import CrawlingSequence

crawling_sequences: Table = get_schema('crawling_sequences')


class CrawlingSequenceDao:
    @staticmethod
    async def get_last_by_job_name(job_name: str) -> CrawlingSequence:
        query = crawling_sequences.select().where(crawling_sequences.c.job_name == job_name)\
            .order_by(desc(crawling_sequences.c.created_at))
        return await db.fetch_one(query)

    @staticmethod
    async def insert(job_name: str) -> int:
        now = datetime.utcnow()
        timestamp = int(now.timestamp() * 1000)
        query = crawling_sequences.insert()\
            .values(job_name=job_name, timestamp=timestamp, created_at=now, updated_at=now)
        return await db.execute(query)
