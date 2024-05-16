from pydantic import BaseModel, constr

class TaskModel(BaseModel):
    title:str = constr(min_length=4, max_length=15, pattern=r'^[a-zA-Z0-9]+$')
    description: str = None
    completed: bool = False

class UpdateTaskModel(BaseModel):
    description: str = None
    completed: bool = False