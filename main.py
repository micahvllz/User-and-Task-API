from fastapi import FastAPI, Depends
from router import userRouter

import models
from database import engine

models.Base.metadata.create_all(bind=engine)

import uuid

app = FastAPI()

app.include_router(userRouter.router)

# admin = {
#     "username": "admin", 
#     "password": "admin"
# }



# @app.get("/login")
# def index():
#     return admin

# @app.post('/login')
# def loginUser(log: AdminLog):
#     if admin['username'] == log.username:
#         if admin['password'] == log.password:
#             admin['log_id'] = uuid.uuid4()
#             return {"Sucess": "User successfully logged in"}
#         if 'log_id' in admin:
#             del admin['log_id']
#         return {"Error": "Incorrect Password"}
#     if 'log_id' in admin:
#         del admin['log_id']
#     return {"Error": "Username does not exist"}
