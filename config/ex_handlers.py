import logging

from fastapi import HTTPException, exception_handlers
from starlette.requests import Request
from starlette.responses import JSONResponse


async def custom_http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    headers = getattr(exc, "headers", None)
    logging.error(f'"{request.method} {request.url}" request is failed. '
                  f'exception: {exc.status_code} {exc.detail}')
    return await exception_handlers.http_exception_handler(request, exc)
