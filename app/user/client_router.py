from fastapi import APIRouter, Body
from starlette.responses import JSONResponse

from .client_service import ClientService
from .user_service import UserService

client_router = APIRouter()
user_service = UserService()
client_service = ClientService()


@client_router.post('/clients')
async def create_client(email: str = Body(...), password: str = Body(...)):
    user = await user_service.authenticate_user(email, password)
    client_id, client_secret = await client_service.create_client(user.id)
    return JSONResponse({
        'client_id': client_id,
        'client_secret': client_secret
    })
