from bson import ObjectId
from datetime import date

def task_serializer(task: dict) -> dict:
    print(task.get('created_at'))
    return {
        'id': str(ObjectId(task.get('_id'))),
        'title': task.get('title'),
        'description': task.get('description') or "",
        'completed': task.get('completed'),
        'created_at': str(task.get('created_at')),
        'updated_at': strdate(task.get('updated_at'))
    }
    
def tasks_serializer(tasks: list) -> list:
    return [task_serializer(task) for task in tasks]
    