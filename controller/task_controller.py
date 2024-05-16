from fastapi import status
from config.database import tasks_db
from model.task import TaskModel
from response import AppResponse
from schema.tasks import task_serializer, tasks_serializer
from typing import Union
from bson import ObjectId
from pymongo import errors

async def list_user_tasks(user_id: str) -> AppResponse:
    try:
        tasks = tasks_db.find({'user_id': user_id})
        tasks = tasks_serializer(tasks)
        return AppResponse(message=f"Tasks ({len(tasks)})", status_code=status.HTTP_200_OK, data={'data': tasks})  if tasks else AppResponse(message="Task empty!", status_code=status.HTTP_200_OK, data={'data': tasks})
    except Exception as e:
        print(e)
        return AppResponse(message="Unable to fetch tasks", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
async def create_task(user_id: str, task: TaskModel) -> AppResponse:
    try:
        new_task = tasks_db.insert_one({'title': task.title, 'description': task.description, 'completed': task.completed, 'user_id': user_id})
        return AppResponse(message="Task Added!", status_code=status.HTTP_200_OK, data={'task_id': str(new_task.inserted_id)})
    except Exception as e:
        print(e)
        return AppResponse(message="Unable add tasks", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

async def find_task(user_id: str, task_id: str) -> Union[dict, bool]:
    try:
        task = tasks_db.find_one({'user_id': user_id, '_id': ObjectId(task_id)})
        return task_serializer(task) if task else False
    except:
        return False

async def task_title_exist(user_id: str, title: str) -> AppResponse:
    ''
    
async def update_task_controller(user_id: str, task: dict) -> AppResponse:
    ""
    
async def delete_task(task_id: str, user_id: str) -> AppResponse:
    try:
        task = await find_task(user_id=user_id, task_id=task_id)
        if not task:
            return AppResponse(message="Invalid task id provided", status_code=status.HTTP_400_BAD_REQUEST)
        # delete task
        tasks_db.delete_one({'_id': ObjectId(task['id'])})
        return AppResponse(message="task deleted!", status_code=status.HTTP_200_OK)
    
    except Exception as e:
        print(e)
        return AppResponse(message="Unable to delete task", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)