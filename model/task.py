from pydantic import BaseModel, constr, root_validator, validator
import re

class TaskModel(BaseModel):
    title:str = constr(min_length=4, max_length=15)
    description: str = None
    @validator('title')
    def title_custom_validator(cls, v):
        if not re.match(r'^[a-zA-Z0-9\s-]+$', v):
            raise ValueError('Title allows (letters, numbers, whitespaces and hypens only).')
        return v


class UpdateTaskModel(BaseModel):
    description: str = None
    completed: bool = None
    
    @root_validator(pre=True)
    def check_non_empty(cls, values):
        if not values.get('description') and values.get('completed') is None:
            raise ValueError('At least one of "description" or "completed" must be provided and cannot be None.')
        return values
    
    def dict_without_none(self):
        """Returns the model as a dictionary without keys that have None values."""
        return {key: value for key, value in self.dict().items() if value is not None}