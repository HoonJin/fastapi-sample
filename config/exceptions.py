import logging
from typing import Any

from fastapi import HTTPException, exception_handlers, Request, status
from fastapi.responses import JSONResponse


class BadRequestException(HTTPException):
    def __init__(self, detail: Any = None, headers: dict = None):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail, headers=headers)


class UnauthorizedException(HTTPException):
    def __init__(self, detail: Any = None, headers: dict = None):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail, headers=headers)


class ForbiddenException(HTTPException):
    def __init__(self, detail: Any = None, headers: dict = None):
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=detail, headers=headers)


class NotFoundException(HTTPException):
    def __init__(self, detail: Any = None, headers: dict = None):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail, headers=headers)


class UnprocessableException(HTTPException):
    def __init__(self, detail: Any = None, headers: dict = None):
        super().__init__(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=detail, headers=headers)


class TooManyRequestException(HTTPException):
    def __init__(self, detail: Any = None, headers: dict = None):
        super().__init__(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail=detail, headers=headers)


class InternalErrorException(HTTPException):
    def __init__(self, detail: Any = None, headers: dict = None):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail, headers=headers)


async def custom_http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    request_id = request.headers.get('X-Request-ID', '')
    logging.error(f"[{request_id}] {request.method} {request.get('path')} request is failed. "
                  f"exception: {exc.status_code} {exc.detail}", exc_info=True)
    return await exception_handlers.http_exception_handler(request, exc)
