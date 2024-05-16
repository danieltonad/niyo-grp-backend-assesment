import jwt
from fastapi import HTTPException, Depends
from time import time
from config.database import users_db
from schema.users import user_serializer
from fastapi.security import OAuth2PasswordBearer
from settings import settings
from fastapi import status
from bson import ObjectId


# Define an instance of OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_VERSION}{settings.OAUTH_URL}")


def token_response(token: str):
    return {
        'access_token': token
    }

def generate_access_token(user: dict):
    # remove password from dict
    user.pop('password')
    
    # jwt payload
    payload = {
        'user': user,
        'expiry': time() + settings.ACCESS_TOKEN_EXPIRE
    }
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    return token_response(token)

# todo
def refresh_access_token(token: str):
    try:
        user = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        if user['expiry'] >= time():
            return generate_access_token(user)
        else:
            return False

    except:
         return False

def decode_access_token(token: str = Depends(oauth2_scheme)):
    try:
        decoded_token = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        if decoded_token.get('expiry') >= time():
            user = decoded_token['user']
            user = user_serializer(users_db.find_one({'_id': ObjectId(user['id'])}))
            return user
        else:
            raise

    except:
        raise HTTPException(detail='user not authenticated', status_code=status.HTTP_401_UNAUTHORIZED)
