from config.database import users_db
from fastapi import status
from schema.users import user_serializer
from utilities.auth_utils import hash_pwd
from .jwt import generate_access_token

async def login_user_controller(username: str, password:str):
    try:
        user = users_db.find_one({'username': username, 'password': hash_pwd(password)})
        if user:
            token = await generate_access_token(user)
            return token
        else:
            return {'detail': 'invalid user credentials'}
    except:
        return {'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'detail': 'Internal Server Error'}
    

async def register_user_controller(username: str, password: str):
    try:
        user = users_db.insert_one({'username': username, 'password': password})
        return user
    except Exception as e:
        print(e)
        return {'status': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': 'user created!'}
    