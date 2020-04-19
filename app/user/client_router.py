from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer

from .domains import LoginForm, ClientForm
from .entities import User
from .client_service import ClientService

client_router = APIRouter()
client_service = ClientService()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    return await client_service.get_user_by_access_token(token)


@client_router.post('/clients')
async def create_client(user: User = Depends(get_current_user)):
    client_id, client_secret = await client_service.create_client(user)
    return JSONResponse({
        'client_id': client_id,
        'client_secret': client_secret
    })


@client_router.post('/access_token')
async def create_access_token(form_data: ClientForm = Depends()):
    return await client_service.create_access_token(form_data)


@client_router.post('/login')
async def login(form_data: LoginForm = Depends()):
    return await client_service.login(form_data)


@client_router.get('/token_test')
async def token_test(user: User = Depends(get_current_user)):
    return user
