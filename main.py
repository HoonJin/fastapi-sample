import logging
from datetime import datetime

import uvicorn
from fastapi import FastAPI, HTTPException, Request, Depends

from app.test import test_router
from config import conf, ex_handlers
from database import db

ENV = conf.get('ENV', str, 'dev')
app = FastAPI(
    debug=True if ENV == 'dev' else conf.get('DEBUG', bool, False),
    docs_url='/docs' if ENV == 'dev' else None,
    openapi_url='/openapi.json' if ENV == 'dev' else None,
)
app.add_exception_handler(HTTPException, ex_handlers.custom_http_exception_handler)


# @app.middleware("http")
# async def __request_logging(req: Request, call_next: Callable) -> Response:
#     request_id = req.headers.get('X-Request-ID', '')
#     if req.method == "POST":
#         request_info = f"body: {(await req.body()).decode('UTF-8')}"
#     elif req.method == "PUT" or req.method == "DELETE":
#         request_info = f"path_params: {req.path_params}, body: {(await req.body()).decode('UTF-8')}"
#     else:  # GET
#         request_info = f"query_params: {req.query_params}"
#     logging.info(f"[{request_id}][{datetime.utcnow()}]<{req.method} {req.get('path')}> {request_info}")
#
#     res = await call_next(req)
#     logging.info(f"[{request_id}][{datetime.utcnow()}] code: {res.status_code}, headers: {res.headers}")
#     return res

async def __request_logging(req: Request):
    request_id = req.headers.get('X-Request-ID', '')
    if req.method == "POST":
        request_info = f"body: {(await req.body()).decode('UTF-8')}"
    elif req.method == "PUT" or req.method == "DELETE":
        request_info = f"path_params: {req.path_params}, body: {(await req.body()).decode('UTF-8')}"
    else:  # GET
        request_info = f"query_params: {req.query_params}"
    logging.info(f"[{request_id}][{datetime.utcnow()}]<{req.method} {req.get('path')}> {request_info}")


app.include_router(test_router, tags=['tests'], dependencies=[Depends(__request_logging)])


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
    uvicorn.run(app, host='127.0.0.1', port=8000, log_level=LOG_LEVEL, debug=True)
