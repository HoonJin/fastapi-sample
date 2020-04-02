from typing import List, Optional

from database import db, get_schema
from .domains import Test

tests = get_schema('tests')


class TestDao:
    @staticmethod
    async def get_all() -> List[Test]:
        query = tests.select()
        return list(map(lambda x: Test(**x), await db.fetch_all(query)))

    @staticmethod
    async def get_all_count() -> int:
        query = tests.count()
        return await db.fetch_val(query)

    @staticmethod
    async def get_all_with_offset_and_limit(offset: int, limit: int) -> List[Test]:
        query = tests.select().offset(offset).limit(limit)
        return list(map(lambda x: Test(**x), await db.fetch_all(query)))

    @staticmethod
    async def get_by_id(test_id: int) -> Test:
        query = tests.select().where(tests.c.id == test_id)
        return Test(** await db.fetch_one(query))

    @staticmethod
    async def find_by_id(test_id: int) -> Optional[Test]:
        query = tests.select().where(tests.c.id == test_id)
        # 코드를 예쁘게 보일 방법을 찾아봐야함
        result = await db.fetch_one(query)
        return Test(**result) if result is not None else None

    @staticmethod
    async def delete_by_id(test_id: int):
        query = tests.delete().where(tests.c.id == test_id)
        result = await db.execute(query)
        return result
