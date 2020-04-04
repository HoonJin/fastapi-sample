import uvicorn
from fastapi import FastAPI, HTTPException

from config import conf, ex_handlers
from database import db
from test import test_router

ENV = conf.get('ENV', str, 'dev')
app = FastAPI(
    docs_url='/docs' if ENV == 'dev' else None,
    openapi_url='/openapi.json' if ENV == 'dev' else None
)
app.include_router(test_router, tags=['tests'])

app.add_exception_handler(HTTPException, ex_handlers.custom_http_exception_handler)


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


@app.get('/test', status_code=403)
async def forbidden():
    return {}


if __name__ == '__main__':
    LOG_LEVEL = conf.get('LOG_LEVEL', str, 'info')
    uvicorn.run(app, host='127.0.0.1', port=8000, log_level=LOG_LEVEL)
