
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer

from .client_router import get_current_user
from .domains import UserCreate
from .entities import User
from .user_service import UserService

user_router = APIRouter()
user_service = UserService()


@user_router.post('/users')
async def sign_up(create: UserCreate):
    user_id = await user_service.sign_up(create)
    return JSONResponse({'id': user_id})


@user_router.get('/users')
async def get_me(user: User = Depends(get_current_user)):
    return user
