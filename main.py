from fastapi import FastAPI

from database import db, tests
from database.test_dao import TestDao

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


@app.get("/test")
async def test1():
    # query = tests.select().where(tests.c.id == 1)
    # query = tests.select().where(tests.c.id.in_([1, 2]))
    # result = await db.fetch_all(query)
    result = await TestDao.find_by_id(4)
    # result = await TestDao.get_all()
    # print(list(map(lambda x: x.created, result)))
    return result
