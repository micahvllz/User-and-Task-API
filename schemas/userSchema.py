from datetime import datetime as dt
from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    age: int

# Schema for request body
class CreateUser(UserBase):
    password: str

# Schema for response body
class User(UserBase):
    created_at: dt
    updated_at: dt