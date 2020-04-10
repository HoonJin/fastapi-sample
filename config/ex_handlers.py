import logging

from fastapi import HTTPException, exception_handlers, Request
from fastapi.responses import JSONResponse


async def custom_http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    request_id = request.headers.get('X-Request-ID', '')
    logging.error(f"[{request_id}] {request.method} {request.get('path')} request is failed. "
                  f"exception: {exc.status_code} {exc.detail}")
    return await exception_handlers.http_exception_handler(request, exc)
