from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from router import authRouter, userRouter, taskRouter
from database import get_db
from models.taskModel import Task

# Register template folder
template = Jinja2Templates('templates')

app = FastAPI()

# Register Routes
app.include_router(authRouter.router)
app.include_router(userRouter.router)
app.include_router(taskRouter.router)