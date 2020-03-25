from fastapi import FastAPI
from test import test_router

from database import db

app = FastAPI()
app.include_router(test_router, tags=['tests'])


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
