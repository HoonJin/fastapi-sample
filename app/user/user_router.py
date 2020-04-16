
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from starlette import status

from .client_dao import ClientDao
from .client_service import ClientService
from .domains import UserCreate
from .user_dao import UserDao
from .user_service import UserService

user_router = APIRouter()
user_service = UserService()
client_service = ClientService()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


@user_router.post('/users')
async def sign_up(create: UserCreate):
    user_id = await user_service.sign_up(create)
    return JSONResponse({'id': user_id})


@user_router.post('/token')
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await user_service.authenticate_user(form_data.username, form_data.password)
    client = await client_service.get_client(form_data.client_id, form_data.client_secret)
    if user.id == client.user_id:
        return JSONResponse({'access_token': client.client_id})
    else:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED)


@user_router.get('/users')
async def get_me(token: str = Depends(oauth2_scheme)):
    client = await ClientDao.find_by_client_id(token)
    if client is None:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)

    user = await UserDao.get_by_id(client.user_id)
    return user
