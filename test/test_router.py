from typing import List

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND

from .test_dao import TestDao
from .domains import Test

test_router = APIRouter()


@test_router.get('/tests', tags=['tests'], response_model=List[Test])
async def test1():
    # query = tests.select().where(tests.c.id == 1)
    # query = tests.select().where(tests.c.id.in_([1, 2]))
    # result = await db.fetch_all(query)
    result = await TestDao.get_all()
    # print(list(map(lambda x: x.created, result)))
    return result


@test_router.get('/tests/{t_id}', tags=['tests'], response_model=Test)
async def test2(t_id: int):
    result = await TestDao.find_by_id(t_id)
    return result if result is not None else JSONResponse(status_code=HTTP_404_NOT_FOUND, content={})


@test_router.get('/tests1')
async def test3(request: Request):
    # j = await request.json()
    # print(j)
    params = request.query_params
    b = await request.body()
    print(b.decode())
    return {}

    # try:
    #     return await TestDao.get_by_id(t_id)
    # except Exception as e:
    #     raise HTTPException(status_code=HTTP_404_NOT_FOUND)

    # if result is not None:
    #     return result
    # else:
    #     return JSONResponse(status_code=404, content={})
