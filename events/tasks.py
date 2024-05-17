from fastapi import Request
from asyncio import sleep, Queue, CancelledError
from utilities.task_utils import remove_subscriber_by_user_id
from typing import List, Dict


async def event_generator(user_id: str, request: Request, subscribers: List[Dict[str,Queue]]):
        queue = Queue()
        subscribers.append({'user_id': user_id, 'subscriber': queue})
        print(subscribers)
        try:
            while True:
                if await request.is_disconnected():
                    subscribers = remove_subscriber_by_user_id(user_id=user_id, subscribers=subscribers)
                    break
                # task = await queue.get()
                # print(task)
                yield f"event: Tasks\ndata: {i}\n\n"
                await sleep(1)
                # for i in range(1,20):
                #     yield f"event: Tasks\ndata: {i}\n\n"
                #     await sleep(1)
        except CancelledError:
            subscribers = remove_subscriber_by_user_id(user_id=user_id, subscribers=subscribers)