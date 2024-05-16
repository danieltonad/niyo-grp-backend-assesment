from fastapi import status
from config.database import tasks_db
from model.task import TaskModel
from response import AppResponse


async def create_task_controller(user_id: str, task: TaskModel) -> AppResponse:
    try:
        new_task = tasks_db.insert_one({'title': task.title, 'description': task.description, 'completed': task.completed, 'user_id': user_id})
        return AppResponse(message="Task created!", status_code=status.HTTP_200_OK, data={'task_id': str(new_task.inserted_id)})
    except Exception as e:
        print(e)

async def task_title_exist(user_id: str, title: str):
    ''
    
async def update_task_controller(user_id: str, task: dict):
    ""