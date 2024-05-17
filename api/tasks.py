from fastapi import APIRouter, Depends, Request, BackgroundTasks
from controller.auth.jwt import decode_access_token
from model.task import TaskModel, UpdateTaskModel
from controller.task_controller import list_user_tasks, create_task, delete_task, update_task, find_task
from fastapi.responses import StreamingResponse
from events.tasks import event_generator

tasks = APIRouter()


@tasks.get('/tasks', tags=['List User Tasks'])
async def get_user_tasks_route(user: dict = Depends(decode_access_token)):
    """list user tasks endpoint"""
    return await list_user_tasks(user_id=user['id'])

@tasks.post('/task', tags=['Add Tasks'])
async def add_user_tasks_route(task: TaskModel, background_task: BackgroundTasks, user: dict = Depends(decode_access_token)):
    """create user tasks endpoint"""
    return await create_task(user_id=user['id'], task=task, background_task=background_task)

@tasks.patch('/task/{id}', tags=['Update Tasks'])
async def update_user_tasks_route(id: str, task: UpdateTaskModel, background_task: BackgroundTasks, user: dict = Depends(decode_access_token)) -> bool:
    """update user tasks endpoint"""
    return await update_task(user_id=user['id'], task_id=id, task=task, background_task=background_task)

@tasks.get('/task/{id}', tags=['Find Tasks'])
async def find_user_tasks_route(id: str, user: dict = Depends(decode_access_token)) -> bool:
    """find user tasks endpoint"""
    return await find_task(user_id=user['id'], task_id=id)

@tasks.delete('/task/{id}', tags=['Delete Tasks'])
async def delete_user_tasks_route(id: str, background_task: BackgroundTasks, user: dict = Depends(decode_access_token)):
    """delete user tasks endpoint"""
    return await delete_task(task_id=id, user_id=user['id'], background_task=background_task)

# subscribe endpoint
@tasks.get('/stream/tasks')
async def stream_task_route(request: Request, user: dict = Depends(decode_access_token)):
    """SSE user stream endpoint"""
    return StreamingResponse(event_generator(user_id=user['id'], request=request), media_type="text/event-stream")