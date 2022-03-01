from pydantic import BaseModel

class AdminLog(BaseModel):
    username: str
    password: str

class UserForm(BaseModel):
    name: str
    age: int