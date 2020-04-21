
from fastapi import APIRouter, Depends, Body, Query
from fastapi.responses import JSONResponse

from .client_router import get_current_user
from .entities import User
from .user_service import UserService

user_router = APIRouter()
user_service = UserService()


@user_router.post('/users')
async def sign_up(email: str = Body(...), password: str = Body(...)):
    user_id = await UserService.sign_up(email, password)
    return JSONResponse({'id': user_id})


@user_router.get('/users')
async def get_me(user: User = Depends(get_current_user)):
    return user


@user_router.get('/confirm')
async def confirm(token: str = Query(...)):
    await UserService.confirm(token)
    return JSONResponse({})
