import uvicorn
from fastapi import FastAPI

from config import conf
from database import db
from test import test_router

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


if __name__ == '__main__':
    log_level = conf.get('LOG_LEVEL', str, 'info')
    uvicorn.run(app, host='127.0.0.1', port=8000, log_level=log_level)
