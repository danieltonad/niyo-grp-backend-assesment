from typing import Union
from asyncio import Queue
from settings import settings

def remove_subscriber_by_user_id(user_id: str):
    settings.subscribers = [subscriber for subscriber in settings.subscribers if subscriber.get('user_id') != user_id]
    
def get_subscriber_by_user_id(user_id: str) -> Union[Queue, bool]:
    for subscriber in settings.subscribers:
        if subscriber.get('user_id') == user_id:
            return subscriber.get('subscriber')
    return False