from pydantic import BaseModel

class TokenData(BaseModel):
    name: str
    age: str

class AuthForm(BaseModel):
    name: str
    password: str
