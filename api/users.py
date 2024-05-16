from fastapi import APIRouter, Depends
from model.user import UserModel
from settings import settings
from controller.auth.auth import login_user_controller, register_user_controller
from fastapi.security import OAuth2PasswordRequestForm

users = APIRouter()

@users.post('/register',tags=['Register User'] ,response_model="")
async def register_user_route(data: UserModel):
    """ user registraton endpoint """
    data = dict(data)
    print(data)
    return await register_user_controller(username=data.get('username'), password=data.get('password'))

@users.post('/login',tags=['Login User'] ,response_model="")
async def login_user_route(data: UserModel):
    """ user registraton endpoint """
    return ""

@users.post(settings.OAUTH_URL,tags=['Login User'] ,response_model="")
async def o_login_user_route(form_data: OAuth2PasswordRequestForm = Depends()):
    return await login_user_controller(email_or_username=form_data.username, password=form_data.password)