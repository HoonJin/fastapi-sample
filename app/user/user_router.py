
from fastapi import APIRouter, status, Body, Query, Path
from fastapi.responses import JSONResponse

from .domains import UserCreate
from .user_service import UserService

user_router = APIRouter()
user_service = UserService()


@user_router.post('/users')
async def sign_up(create: UserCreate):
    user_id = await user_service.sign_up(create)
    return JSONResponse({'id': user_id})
