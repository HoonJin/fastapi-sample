
from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse

from .client_service import ClientService
from .domains import UserCreate
from .user_service import UserService

user_router = APIRouter()
user_service = UserService()
client_service = ClientService()


@user_router.post('/users')
async def sign_up(create: UserCreate):
    user_id = await user_service.sign_up(create)
    return JSONResponse({'id': user_id})


@user_router.post('/users/verify')
async def verify(email: str = Body(...), password: str = Body(...)):
    user = await user_service.authenticate_user(email, password)
    client_id, client_secret = await client_service.create_client(user.id)
    return JSONResponse({
        'client_id': client_id,
        'client_secret': client_secret
    })

