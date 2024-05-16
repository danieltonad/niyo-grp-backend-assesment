from config.database import users_db
from fastapi import status
from schema.users import user_serializer
from utilities.auth_utils import hash_pwd
from .jwt import generate_access_token
from response import AppResponse

async def login_user_controller(username: str, password:str):
    try:
        user = users_db.find_one({'username': username, 'password': hash_pwd(password)})
        if user:
            token = await generate_access_token(user)
            return AppResponse(message="login successfull!", status_code=status.HTTP_200_OK, data=token)
        else:
            return AppResponse(message="incorrect user credentials!", status_code=status.HTTP_403_FORBIDDEN)
    except Exception as e:
        return AppResponse(message="Unable to login!", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

async def register_user_controller(username: str, password: str):
    try:
        users_db.insert_one({'username': username, 'password': hash_pwd(password)})
        return AppResponse(message="User account created", status_code=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return AppResponse(message="Unable to create account!", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    