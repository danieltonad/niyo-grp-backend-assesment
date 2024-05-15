from pydantic import BaseModel, constr

class UserModel(BaseModel):
    username: constr(min_length=6, max_length=15, pattern=r'^[a-zA-Z0-9]+$')
    password: constr(min_length=6)