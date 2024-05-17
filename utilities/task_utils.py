from typing import List, Dict
from asyncio import Queue

def remove_subscriber_by_user_id(user_id: str, subscribers: List[Dict[str,Queue]]) -> List[Dict[str,Queue]]:
    return [subscriber for subscriber in subscribers if subscriber.get('user_id') != user_id]