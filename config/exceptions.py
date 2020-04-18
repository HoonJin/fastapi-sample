from http import HTTPStatus
import logging
from typing import Any

from fastapi import Request, status
from fastapi.responses import JSONResponse


class HTTPException(Exception):
    def __init__(self, status_code: int, code: str, detail: str = None) -> None:
        self.status_code = status_code
        self.code = code
        if detail is None:
            http_status = HTTPStatus(status_code)
            self.detail = f'{http_status.phrase}: {http_status.description}'
        else:
            self.detail = detail

    def __str__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}(status_code={self.status_code!r}, code={self.code!r}, detail={self.detail!r})"


class BadRequestException(HTTPException):
    def __init__(self, code='bad_request', detail: Any = None):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, code=code, detail=detail)


class UnauthorizedException(HTTPException):
    def __init__(self, code='unauthorized', detail: Any = None):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, code=code, detail=detail)


class ForbiddenException(HTTPException):
    def __init__(self, code='forbidden', detail: Any = None):
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, code=code, detail=detail)


class NotFoundException(HTTPException):
    def __init__(self, code='not_found', detail: Any = None):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, code=code, detail=detail)


class UnprocessableException(HTTPException):
    def __init__(self, code='unprocessable_entity', detail: Any = None):
        super().__init__(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, code=code, detail=detail)


class TooManyRequestException(HTTPException):
    def __init__(self, code='too_many_request', detail: Any = None):
        super().__init__(status_code=status.HTTP_429_TOO_MANY_REQUESTS, code=code, detail=detail)


class InternalErrorException(HTTPException):
    def __init__(self, code='internal_server_error', detail: Any = None):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, code=code, detail=detail)


# 추후에 모든 익셉션을 처리할 수 있도록 Exception 타입을 받는 방식으로 만듬
async def custom_http_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    request_id = request.headers.get('X-Request-ID', '')
    if isinstance(exc, HTTPException):
        logging.warning(f"[{request_id}] {request.method} {request.url.path} request is failed. {exc}")
        return JSONResponse({"code": exc.code, "detail": exc.detail}, status_code=exc.status_code)
    else:
        logging.error(f"[{request_id}] {request.method} {request.url.path} request is failed. ", exc_info=True)
        return JSONResponse({"code": 'internal_server_error', "detail": str(exc)},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
