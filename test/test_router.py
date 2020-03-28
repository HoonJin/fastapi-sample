from typing import List

from fastapi import APIRouter, HTTPException, Request
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
async def test3(request: Request):
    params = request.query_params
    page = int(params.get('page'))
    per_page = int(params.get('per_page'))
    return await test_service.get_all_pagination(page, per_page)

    # try:
    #     return await TestDao.get_by_id(t_id)
    # except Exception as e:
    #     raise HTTPException(status_code=HTTP_404_NOT_FOUND)

    # if result is not None:
    #     return result
    # else:
    #     return JSONResponse(status_code=404, content={})


@test_router.get('/tests/{t_id}', tags=['tests'], response_model=Test)
async def get(t_id: int):
    result = await TestDao.find_by_id(t_id)
    return result if result is not None else JSONResponse(status_code=HTTP_404_NOT_FOUND, content={})