from typing import List

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND

from .test_dao import TestDao
from .domains import Test
from .test_service import TestService

test_router = APIRouter()
test_service = TestService()


@test_router.get('/tests', tags=['tests'], response_model=List[Test])
async def get_all():
    result = await TestDao.get_all()
    return result


@test_router.get('/tests/pagination')
async def get_by_pagination(page: int = 1, per_page: int = 20):
    return await test_service.get_all_pagination(page, per_page)


@test_router.get('/tests/{t_id}', tags=['tests'], response_model=Test)
async def get(t_id: int):
    result = await TestDao.find_by_id(t_id)
    return result if result is not None else JSONResponse(status_code=HTTP_404_NOT_FOUND, content={})

    # try:
    #     return await TestDao.get_by_id(t_id)
    # except Exception as e:
    #     raise HTTPException(status_code=HTTP_404_NOT_FOUND)

    # if result is not None:
    #     return result
    # else:
    #     return JSONResponse(status_code=404, content={})
