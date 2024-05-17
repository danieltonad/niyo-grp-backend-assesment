from fastapi import status
from config.database import tasks_db
from model.task import TaskModel, UpdateTaskModel
from response import AppResponse
from schema.tasks import task_serializer, tasks_serializer
from typing import Union
from bson import ObjectId
from pymongo import errors
from events.tasks import trigger_changes

async def get_user_tasks(user_id: str) -> list:
    return tasks_serializer(tasks_db.find({'user_id': user_id}))

async def list_user_tasks(user_id: str) -> AppResponse:
    try:
        tasks = get_user_tasks(user_id)
        return AppResponse(message=f"Tasks ({len(tasks)})", status_code=status.HTTP_200_OK, data={'data': tasks})  if tasks else AppResponse(message="Task empty!", status_code=status.HTTP_200_OK, data={'data': tasks})
    except Exception as e:
        print(e)
        return AppResponse(message="Unable to fetch tasks", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
   
    
async def create_task(user_id: str, task: TaskModel) -> AppResponse:
    try:
        new_task = tasks_db.insert_one({'title': task.title, 'description': task.description, 'completed': False, 'user_id': user_id})
        await trigger_changes(user_id)
        return AppResponse(message="Task Added!", status_code=status.HTTP_200_OK, data={'task_id': str(new_task.inserted_id)})
    except errors.DuplicateKeyError:
        return AppResponse(message=f"Task with title `{task.title}` already exist", status_code=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return AppResponse(message="Unable add tasks", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


async def find_task(user_id: str, task_id: str) -> Union[dict, bool]:
    try:
        task = tasks_db.find_one({'user_id': user_id, '_id': ObjectId(task_id)})
        return task_serializer(task) if task else False
    except:
        return False
 
      
async def update_task(user_id: str, task_id: str, task: UpdateTaskModel) -> AppResponse:
    try:
        _task = await find_task(user_id=user_id, task_id=task_id)
        if not _task:
            return AppResponse(message="Invalid task id provided", status_code=status.HTTP_400_BAD_REQUEST)
        print(task.dict_without_none())
        tasks_db.update_one({'_id': ObjectId(task_id)}, {
            "$set": task.dict_without_none()
        })
        return AppResponse(message="Task updated!", status_code=status.HTTP_200_OK)
        
    except Exception as e:
        print(e)
        return AppResponse(message="Unable to update task", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
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