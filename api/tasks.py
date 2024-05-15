from fastapi import APIRouter
# from 

tasks = APIRouter()

@tasks.get('/tasks', tags=['List User Tasks'], response_model="")
async def get_user_tasks_route():
    """list user tasks endpoint"""
    return ""

@tasks.post('/task', tags=['Add Tasks'], response_model="")
async def add_user_tasks_route():
    """create user tasks endpoint"""
    return ""

@tasks.put('/task/{id}', tags=['Update Tasks'], response_model="")
async def update_user_tasks_route(id: str):
    """update user tasks endpoint"""
    return ""

@tasks.delete('/task/{id}', tags=['Delete Tasks'], response_model="")
async def delete_user_tasks_route(id: str):
    """delete user tasks endpoint"""
    return ""