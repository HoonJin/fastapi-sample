from typing import List

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND

from database import db
from .test_dao import TestDao
from .domains import Test
from .test_service import TestService

test_router = APIRouter()
test_service = TestService()


@test_router.get('/tests', tags=['tests'], response_model=List[Test])
async def get_all():
    result = await TestDao.get_all()
    return result


@test_router.get('/tests/{t_id:int}', tags=['tests'], response_model=Test)
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


@test_router.get('/tests/pagination')
async def get_by_pagination(page: int = 1, per_page: int = 20):
    return await test_service.get_all_pagination(page, per_page)


@test_router.delete('/tests/{t_id:int}', tags=['tests'], response_model=None)
async def delete(t_id: int):
    async with db.transaction() as t:
        await TestDao.delete_by_id(t_id)
    # transaction = await db.transaction()
    # try:
    #     await TestDao.delete_by_id(t_id)
    #     # await transaction.commit()
    # except Exception as e:
    #     print('asdfasfdaf')
    #     print(e)
    #     # await transaction.rollback()
    # finally:
    #     pass
        # transaction.

    # return await TestDao.delete_by_id(t_id)
    # obj = await TestDao.find_by_id(t_id)
    # if obj is not None:
    #     return await TestDao.delete_by_id(obj.id)
    # else:
    #     return JSONResponse(status_code=HTTP_404_NOT_FOUND, content={})
