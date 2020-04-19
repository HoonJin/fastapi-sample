from enum import Enum
from typing import Optional

from fastapi import Form
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel


class UserStatus(str, Enum):
    unconfirmed = 'unconfirmed'
    registered = 'registered'
    dormant = 'dormant'
    terminated = 'terminated'


class UserCreate(BaseModel):
    email: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = 'Bearer'


class LoginForm(OAuth2PasswordRequestForm):
    def __init__(self,
                 username: str = Form(...),
                 password: str = Form(...),
                 service: Optional[str] = Form('viole')
                 ):
        super().__init__("password", username, password, "", None, None)
        self.service = service


class ClientForm(OAuth2PasswordRequestForm):
    def __init__(self,
                 client_id: str = Form(...),
                 client_secret: str = Form(...),
                 ):
        super().__init__("client_credentials", "", "", "", client_id, client_secret)
