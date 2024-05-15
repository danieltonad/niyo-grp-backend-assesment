from fastapi import APIRouter
# from 

users = APIRouter()

@users.post('/register',tags=['Register User'] ,response_model="")
async def register_user_route(data):
    """ user registraton endpoint """
    return ""

@users.post('/login',tags=['Login User'] ,response_model="")
async def login_user_route(data):
    """ user registraton endpoint """
    return ""