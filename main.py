from fastapi import FastAPI
from fastapi.responses import JSONResponse

from database import db
from test import TestDao

app = FastAPI()


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


@app.get("/")
async def root():
    result = {"hello": "world"}
    return result


@app.get("/tests")
async def test1():
    # query = tests.select().where(tests.c.id == 1)
    # query = tests.select().where(tests.c.id.in_([1, 2]))
    # result = await db.fetch_all(query)
    result = await TestDao.get_all()
    # print(list(map(lambda x: x.created, result)))
    return result


@app.get("/tests/{t_id}")
async def test2(t_id):
    result = await TestDao.find_by_id(t_id)
    return result if result is not None else JSONResponse(status_code=404, content={})
    # if result is not None:
    #     return result
    # else:
    #     return JSONResponse(status_code=404, content={})
