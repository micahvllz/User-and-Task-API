from fastapi import APIRouter, Depends, HTTPException, Cookie
from sqlalchemy.orm import Session
from schemas.userSchema import UserBase
from models.userModel import User
from database import get_db
from dependencies import get_token

router = APIRouter(
    prefix='/users',
    tags=['users'],
    dependencies=[Depends(get_token)]
)

@router.get('/')
def get_the_list_of_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return {'users': users}

@router.get('/{id}')
def get_user_details(id: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(404, 'User not found')
    return {'user': user}

@router.post('/')
def create(user: UserBase, db: Session = Depends(get_db)):
    to_store = User(
        name = user.name,
        age = user.age,
        email = user.email
    )

    db.add(to_store)
    db.commit()
    return {'message': 'User stored successfully.'}

@router.put('/{id}')
def update(id: str, user: UserBase, db: Session = Depends(get_db)): 
    if not db.query(User).filter(User.id == id).update({
        'name': user.name,
        'age': user.age,
        'email': user.email
    }):
        raise HTTPException(404, 'User to update is not found')
    db.commit()
    return {'message': 'User updated successfully.'}

@router.delete('/{id}')
def delete(id: str, db: Session = Depends(get_db)):
    if not db.query(User).filter(User.id == id).delete():
        raise HTTPException(404, 'User to delete is not found')
    db.commit()
    return {'message': 'User removed successfully.'}

