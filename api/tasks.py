from fastapi import APIRouter, Depends, Request
from controller.auth.jwt import decode_access_token
from model.task import TaskModel, UpdateTaskModel
from controller.task_controller import list_user_tasks, create_task, delete_task, update_task
from asyncio import Queue, sleep, CancelledError
from typing import Set
from fastapi.responses import StreamingResponse
import json

tasks = APIRouter()

subscribers: Set[Queue] = set()

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
    # async def event_generator():
    #     queue = Queue()
    #     subscribers.append(queue)
        
    #     try:
    #         while True:
    #             if await request.is_disconnected():
    #                 break
    #             tasks = await queue.get()
    #             print(tasks)
    #             yield f"tasks update"
    #     except CancelledError:
    #         subscribers.remove(queue)
    return StreamingResponse(waypoints_generator, media_type="text/event-stream")

async def waypoints_generator():
    for waypoint in range(1,10):
        data = json.dumps(waypoint)
        yield f"event: locationUpdate\ndata: {data}\n\n"
        await sleep(1)