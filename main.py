from fastapi import FastAPI

from database import db, test

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
    query = test.select()
    result = await db.fetch_all(query)
    return result
