from fastapi import APIRouter, Depends, Request
from controller.auth.jwt import decode_access_token
from model.task import TaskModel, UpdateTaskModel
from controller.task_controller import list_user_tasks, create_task, delete_task, update_task
from asyncio import Queue, sleep, CancelledError
from typing import List, Dict
from fastapi.responses import StreamingResponse
from utilities.task_utils import remove_subscriber_by_user_id
import json

tasks = APIRouter()

subscribers: List[Dict[str,Queue]]= []
# subscribers.append({'user_id': "user['id']", 'subscriber': Queue()})

@tasks.get('/tasks', tags=['List User Tasks'])
async def get_user_tasks_route(user: str = Depends(decode_access_token)):
    """list user tasks endpoint"""
    return await list_user_tasks(user_id=user['id'])

@tasks.post('/task', tags=['Add Tasks'])
async def add_user_tasks_route(task: TaskModel, user: str = Depends(decode_access_token)):
    """create user tasks endpoint"""
    return await create_task(user_id=user['id'], task=task)

@tasks.patch('/task/{id}', tags=['Update Tasks'])
async def update_user_tasks_route(id: str, task: UpdateTaskModel, user: str = Depends(decode_access_token)) -> bool:
    """update user tasks endpoint"""
    return await update_task(user_id=user['id'], task_id=id, task=task)

@tasks.delete('/task/{id}', tags=['Delete Tasks'])
async def delete_user_tasks_route(id: str, user: str = Depends(decode_access_token)):
    """delete user tasks endpoint"""
    return await delete_task(task_id=id, user_id=user['id'])

# subscribe endpoint
@tasks.get('/stream/tasks')
async def stream_task_route(request: Request, user: str = Depends(decode_access_token)):
    return StreamingResponse(event_generator(user_id=user['id'], request=request), media_type="text/event-stream")


async def event_generator(user_id: str, request: Request):
        queue = Queue()
        global subscribers
        subscribers.append({'user_id': user_id, 'subscriber': queue})
        print(subscribers)
        try:
            while True:
                if await request.is_disconnected():
                    subscribers = remove_subscriber_by_user_id(user_id=user_id, subscribers=subscribers)
                    break
                
                for i in range(1,20):
                    yield f"event: Tasks\ndata: {i}\n\n"
                    await sleep(1)
        except CancelledError:
            subscribers = remove_subscriber_by_user_id(user_id=user_id, subscribers=subscribers)