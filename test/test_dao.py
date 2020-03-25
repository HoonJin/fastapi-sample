from typing import List

from database import db
from .domains import *
from .schemas import tests


class TestDao:
    @staticmethod
    async def get_all() -> List[Test]:
        query = tests.select()
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