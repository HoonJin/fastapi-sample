from .test_dao import TestDao


class TestService:
    @staticmethod
    async def get_all_pagination(page: int, per_page: int) -> dict:
        total_cnt = await TestDao.get_all_count()
        total_page = int(total_cnt / per_page) + (0 if total_cnt % per_page == 0 else 1)
        offset = (page - 1) * per_page
        result = await TestDao.get_all_with_offset_and_limit(offset, per_page)
        return {
            'content': result,
            'total_cnt': total_cnt,
            'total_page': total_page
        }
