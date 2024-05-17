from fastapi import Request
from asyncio import sleep, Queue, CancelledError
from utilities.task_utils import remove_subscriber_by_user_id, get_subscriber_by_user_id
from settings import settings
import json


async def event_generator(user_id: str, request: Request):
        queue = Queue()
        settings.subscribers.append({'user_id': user_id, 'subscriber': queue})
        try:
            while True:
                if await request.is_disconnected():
                    remove_subscriber_by_user_id(user_id)
                    break
                task = await queue.get()
                if task:
                    yield f"event: TaskUpdate\ndata:{json.dumps(task)} \n\n"
                    await sleep(1)
        except CancelledError:
            remove_subscriber_by_user_id(user_id)
        
async def trigger_changes(user_id: str):
    subscriber = get_subscriber_by_user_id(user_id)
    if subscriber:
        from controller.task_controller import get_user_tasks
        updated_tasks = await get_user_tasks(user_id)
        await subscriber.put(updated_tasks)