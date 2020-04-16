
from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse

from .domains import UserCreate
from .user_service import UserService

user_router = APIRouter()
user_service = UserService()


@user_router.post('/users')
async def sign_up(create: UserCreate):
    user_id = await user_service.sign_up(create)
    return JSONResponse({'id': user_id})


@user_router.post('/users/verify')
async def verify(email: str = Body(...), password: str = Body(...)):
    result = await user_service.authenticate(email, password)
    return JSONResponse({'result': result})
