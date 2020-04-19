from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from .client_service import ClientService
from .entities import User
from .login_service import get_current_user

client_router = APIRouter()
client_service = ClientService()


@client_router.post('/clients')
async def create_client(user: User = Depends(get_current_user)):
    client_id, client_secret = await client_service.create_client(user)
    return JSONResponse({
        'client_id': client_id,
        'client_secret': client_secret
    })


@client_router.get('/token_test')
async def token_test(user: User = Depends(get_current_user)):
    return user
