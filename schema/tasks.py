def task_serializer(task: dict) -> dict:
    return {
        'title': task.get('title'),
        'description': task.get('description') or "",
    }
    
def tasks_serializer(tasks: list) -> list:
    return [task_serializer(task) for task in tasks]
    