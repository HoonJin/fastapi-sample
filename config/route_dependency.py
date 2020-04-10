import logging

from fastapi import Depends, Request


async def __request_logging(r: Request) -> None:
    request_id = r.headers.get('X-Request-ID', '')
    if r.method == "POST":
        request_info = f"body: {(await r.body()).decode('UTF-8')}"
    elif r.method == "PUT" or r.method == "DELETE":
        request_info = f"path_params: {r.path_params}, body: {(await r.body()).decode('UTF-8')}"
    else:  # GET
        request_info = f"query_params: {r.query_params}"
    logging.info(f"[{request_id}] {r.method} {r.get('path')} {request_info}")


public_dependencies = [Depends(__request_logging)]
