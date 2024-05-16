from fastapi import APIRouter, Depends
from model.user import UserModel
from settings import settings
from controller.auth.auth import login_user_controller, register_user_controller
from fastapi.security import OAuth2PasswordRequestForm

users = APIRouter()

@users.post('/register',tags=['Register User'])
async def register_user_route(data: UserModel):
    """ user registraton endpoint """
    data = dict(data)
    return await register_user_controller(username=data.get('username'), password=data.get('password'))

@users.post('/login',tags=['Login User'])
async def login_user_route(data: UserModel):
    """ user registraton endpoint """
    data = dict(data)
    return await login_user_controller(username=data.get('username'), password=data.get('password'))

@users.post(settings.OAUTH_URL,tags=['OAUTH2 Swagger Login'] ,response_model="")
async def o_login_user_route(form_data: OAuth2PasswordRequestForm = Depends()):
    """oauth2 login for swagger"""
    return await login_user_controller(username=form_data.username, password=form_data.password)