from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models import User
from schemas import AdminLog, UserForm
from database import get_db

router = APIRouter(
    prefix='/users',
    tags=['users']
)

@router.get('/')
def index(db: Session = Depends(get_db)):
    data = db.query(User).all()

    return data

@router.post('/')
def createUser(user: UserForm, db: Session = Depends(get_db)):

    user = User(
        name = user.name,
        age = user.age
    )

    db.add(user)
    db.commit()

    return {
        'message': 'User added successfully!',
        'data': {
            'id': user.id,
            'name': user.name,
            'age': user.age
        }
    }


@router.put('/{id}')
def updateUser(id: int, user: UserForm, db: Session = Depends(get_db)):
    filtered_user = db.query(User).filter(User.id == id).first()

    filtered_user.name = user.name
    filtered_user.age = user.age

    db.commit()

    return {
        'message': 'User updated successfully!',
        'data': {
            'name': filtered_user.name,
            'age': filtered_user.age
        }
    }


@router.delete('/{id}')
def deleteUser(id: int, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.id == id).first()

    if user:
        db.query(User).filter(User.id == id).delete()
        db.commit()
        return {
            'message': 'User deleted successfully!'
        }
    else:
        return {
            'message': 'User not found!'
        }

