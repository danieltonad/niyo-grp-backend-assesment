from fastapi import APIRouter, Depends
from controller.auth.jwt import decode_access_token
from model.task import TaskModel
# from 

tasks = APIRouter()

@tasks.get('/tasks', tags=['List User Tasks'], response_model="")
async def get_user_tasks_route(user: str = Depends(decode_access_token)):
    """list user tasks endpoint"""
    return ""

@tasks.post('/task', tags=['Add Tasks'], response_model="")
async def add_user_tasks_route(data: TaskModel, user: str = Depends(decode_access_token)):
    """create user tasks endpoint"""
    return ""

@tasks.put('/task/{id}', tags=['Update Tasks'], response_model="")
async def update_user_tasks_route(id: str, data: TaskModel, user: str = Depends(decode_access_token)):
    """update user tasks endpoint"""
    return ""

@tasks.delete('/task/{id}', tags=['Delete Tasks'], response_model="")
async def delete_user_tasks_route(id: str, user: str = Depends(decode_access_token)):
    """delete user tasks endpoint"""
    return ""