from fastapi import APIRouter, Depends
from controller.auth.jwt import decode_access_token
from model.task import TaskModel
from controller.task_controller import list_user_tasks, create_task_controller

tasks = APIRouter()

@tasks.get('/tasks', tags=['List User Tasks'])
async def get_user_tasks_route(user: str = Depends(decode_access_token)):
    """list user tasks endpoint"""
    return await list_user_tasks(user_id=user['id'])

@tasks.post('/task', tags=['Add Tasks'])
async def add_user_tasks_route(task: TaskModel, user: str = Depends(decode_access_token)):
    """create user tasks endpoint"""
    return await create_task_controller(user_id=user['id'], task=task)

@tasks.put('/task/{id}', tags=['Update Tasks'])
async def update_user_tasks_route(id: str, data: TaskModel, user: str = Depends(decode_access_token)):
    """update user tasks endpoint"""
    return ""

@tasks.delete('/task/{id}', tags=['Delete Tasks'])
async def delete_user_tasks_route(id: str, user: str = Depends(decode_access_token)):
    """delete user tasks endpoint"""
    return ""