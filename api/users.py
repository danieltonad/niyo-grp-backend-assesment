from fastapi import APIRouter
from model.user import UserModel
from settings import settings

users = APIRouter()

@users.post('/register',tags=['Register User'] ,response_model="")
async def register_user_route(data: UserModel):
    """ user registraton endpoint """
    return ""

@users.post('/login',tags=['Login User'] ,response_model="")
async def login_user_route(data: UserModel):
    """ user registraton endpoint """
    return ""

@users.post(settings.OAUTH_URL,tags=['Login User'] ,response_model="")
async def login_user_route(data: UserModel):
    """ user registraton endpoint """
    return ""