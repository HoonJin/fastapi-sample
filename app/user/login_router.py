from fastapi import APIRouter, Depends

from .domains import ClientForm, LoginForm
from .login_service import LoginService

login_router = APIRouter()


@login_router.post('/access_token')
async def create_access_token(form_data: ClientForm = Depends()):
    return await LoginService.create_access_token(form_data)


@login_router.post('/login')
async def login(form_data: LoginForm = Depends()):
    return await LoginService.login(form_data)
