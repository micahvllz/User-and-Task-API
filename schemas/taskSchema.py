from datetime import datetime as dt
from pydantic import BaseModel

class TaskBase(BaseModel):
    user_id: str
    title: str
    description: str
    is_completed: bool

# Schema for request body
class CreateTask(TaskBase):
    pass

#Schema for response body
class Post(TaskBase):
    created_at: dt
    updated_at: dt