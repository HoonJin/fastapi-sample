import logging

from fastapi import Depends, Request


async def __request_logging(r: Request) -> None:
    # Request 객체 키
    # ['type', 'http_version', 'server', 'client', 'scheme', 'method', 'root_path', 'path', 'raw_path', 'query_string',
    # 'headers', 'fastapi_astack', 'app', 'router', 'endpoint', 'path_params']
    request_id = r.headers.get('X-Request-ID', '')
    # [x for x in r.scope.items()]
    logging.info(f"[{request_id}] {r.method} {r.get('path')} {r.path_params} {r.query_params} {await r.body()}")
    # TODO http method 별로 구분해서 로그 남기기


public_dependencies = [Depends(__request_logging)]
