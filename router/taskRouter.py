from fastapi import APIRouter, Request, Depends, HTTPException, Cookie
from sqlalchemy import or_
from sqlalchemy.orm import Session
from schemas.taskSchema import CreateTask
from models.taskModel import Task
from models.userModel import User
from database import get_db
from dependencies import get_token

router = APIRouter(
    prefix='/tasks',
    tags=['tasks'],
    dependencies=[Depends(get_token)]
)

@router.get('/')
def get_the_list_of_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return {'tasks': tasks}

@router.get('/{id}')
def get_task_details(id: str, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()
    if not task:
        raise HTTPException(404, 'Task not found')
    return {'task': task}

@router.post('/')
def create(task: CreateTask, db: Session = Depends(get_db)):
    to_store = Task(
        user_id = task.user_id,
        title = task.title,
        description = task.description,
        is_completed = task.is_completed
    )

    db.add(to_store)
    db.commit()
    return {'message': 'Task stored successfully.'}

@router.put('/{id}')
def update(id: str, task: CreateTask, db: Session = Depends(get_db)): 
    if not db.query(Task).filter(Task.id == id).update({
        'user_id': task.user_id,
        'title': task.title,
        'description': task.description,
        'is_completed': task.is_completed
    }):
        raise HTTPException(404, 'Task to update is not found')
    db.commit()
    return {'message': 'Task updated successfully.'}

@router.delete('/{id}')
def delete(id: str, db: Session = Depends(get_db)):
    if not db.query(Task).filter(Task.id == id).delete():
        raise HTTPException(404, 'Task to delete is not found')
    db.commit()
    return {'message': 'Task removed successfully.'}
