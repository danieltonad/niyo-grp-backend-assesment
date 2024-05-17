from bson import ObjectId
from datetime import datetime

def task_serializer(task: dict) -> dict:
    return {
        'id': str(ObjectId(task.get('_id'))),
        'title': task.get('title'),
        'description': task.get('description') or "",
        'completed': task.get('completed'),
        'created_at': task.get('created_at').strftime('%d-%m-%Y %H:%M'),
        'updated_at': task.get('updated_at').strftime('%d-%m-%Y %H:%M')
    }
    
def tasks_serializer(tasks: list) -> list:
    return [task_serializer(task) for task in tasks]
    