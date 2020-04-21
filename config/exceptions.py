import logging
from enum import Enum
from typing import Any, Optional

from fastapi import Request, status
from fastapi.responses import JSONResponse


class ErrorCode(str, Enum):
    # 400
    bad_request = 'bad_request'
    invalid_client = 'invalid_client'
    invalid_parameter = 'invalid_parameter'

    # 401
    unauthorized = 'unauthorized'
    token_expired = 'token_expired'

    # 403
    forbidden = 'forbidden'

    # 404
    not_found = 'not_found'

    # 422
    unprocessable_entity = 'unprocessable_entity'

    # 429
    too_many_requests = 'too_many_requests'

    # 500
    internal_server_error = 'internal_server_error'


class HTTPException(Exception):
    def __init__(self, status_code: int, code: ErrorCode, detail: Optional[Any] = None):
        self.status_code = status_code
        self.code = code
        self.detail = detail

    def __str__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}(status_code={self.status_code})(code={self.code}, detail={self.detail})"


class BadRequestException(HTTPException):
    def __init__(self, code=ErrorCode.bad_request, detail: Any = None):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, code=code, detail=detail)


class UnauthorizedException(HTTPException):
    def __init__(self, code=ErrorCode.unauthorized, detail: Any = None):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, code=code, detail=detail)


class ForbiddenException(HTTPException):
    def __init__(self, code=ErrorCode.forbidden, detail: Any = None):
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, code=code, detail=detail)


class NotFoundException(HTTPException):
    def __init__(self, code=ErrorCode.not_found, detail: Any = None):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, code=code, detail=detail)


class UnprocessableException(HTTPException):
    def __init__(self, code=ErrorCode.unprocessable_entity, detail: Any = None):
        super().__init__(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, code=code, detail=detail)


class TooManyRequestException(HTTPException):
    def __init__(self, detail: Any = 'request limit is exceed'):
        super().__init__(status_code=status.HTTP_429_TOO_MANY_REQUESTS, code=ErrorCode.too_many_requests, detail=detail)


class InternalErrorException(HTTPException):
    def __init__(self, detail: Any = None):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                         code=ErrorCode.internal_server_error, detail=detail)


# 추후에 모든 익셉션을 처리할 수 있도록 Exception 타입을 받는 방식으로 만듬
async def custom_http_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    request_id = request.headers.get('X-Request-ID', '')
    if isinstance(exc, InternalErrorException):
        logging.error(f"[{request_id}] {request.method} {request.url.path} request is failed. ", exc_info=True)
        return JSONResponse({"code": exc.code, "detail": exc.detail}, status_code=exc.status_code)
    elif isinstance(exc, HTTPException):
        logging.warning(f"[{request_id}] {request.method} {request.url.path} request is failed. {exc}")
        return JSONResponse({"code": exc.code, "detail": exc.detail}, status_code=exc.status_code)
    else:
        logging.error(f"[{request_id}] {request.method} {request.url.path} request is failed. ", exc_info=True)
        return JSONResponse({"code": ErrorCode.internal_server_error, "detail": str(exc)},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
