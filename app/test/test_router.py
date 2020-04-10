from typing import List

from fastapi import APIRouter, status, Body, Query, Path
from fastapi.responses import JSONResponse

from .domains import Test, TestCreate
from .test_dao import TestDao
from .test_service import TestService

test_router = APIRouter()
test_service = TestService()


@test_router.get('/tests', response_model=List[Test])
async def get_all():
    result = await TestDao.get_all()
    return result


@test_router.get('/tests/{t_id:int}', response_model=Test)
async def get(t_id: int = Path(...)):
    result = await TestDao.find_by_id(t_id)
    return result if result is not None else JSONResponse(status_code=status.HTTP_404_NOT_FOUND)
    # try:
    #     return await TestDao.get_by_id(t_id)
    # except Exception:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@test_router.get('/tests/pagination', description='adsfasdf')
async def get_by_pagination(page: int = Query(1, gt=0), per_page: int = Query(20, gt=0)):
    return await test_service.get_all_pagination(page, per_page)


@test_router.post('/tests')
async def create(test: TestCreate = Body(...)):
    return await TestDao.insert(test.varchar)


@test_router.delete('/tests/{t_id:int}', response_model=None)
async def delete(t_id: int = Path(...)):
    return await test_service.delete(t_id)
