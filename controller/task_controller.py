from fastapi import status
from config.database import tasks_db
from model.task import TaskModel
from response import AppResponse
from schema.tasks import task_serializer, tasks_serializer

async def list_user_tasks(user_id: str) -> AppResponse:
    try:
        tasks = tasks_db.find_one({'user_id': user_id})
        if tasks:
            tasks = tasks_serializer(tasks)
        return AppResponse(message=f"Tasks ({len(tasks)})", status_code=status.HTTP_200_OK, data={'data': tasks})  if tasks else AppResponse(message="Task empty!", status_code=status.HTTP_200_OK, data={'data': []})
    except Exception as e:
        print(e)
        return AppResponse(message="Unable to fetch tasks", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
async def create_task_controller(user_id: str, task: TaskModel) -> AppResponse:
    try:
        new_task = tasks_db.insert_one({'title': task.title, 'description': task.description, 'completed': task.completed, 'user_id': user_id})
        return AppResponse(message="Task Added!", status_code=status.HTTP_200_OK, data={'task_id': str(new_task.inserted_id)})
    except Exception as e:
        print(e)
        return AppResponse(message="Unable add tasks", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

async def task_title_exist(user_id: str, title: str):
    ''
    
async def update_task_controller(user_id: str, task: dict):
    ""