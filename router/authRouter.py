from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from database import get_db
from models.adminModel import Admin
from schemas.authSchema import AuthForm
from jose import jwt
from passlib.context import CryptContext

secret = '663a6bf88c8c876764cd94e445eacd61154424e1eed23b0d3f0befe08bcd646c'
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def password_verify(plain, hashed):
    return pwd_context.verify(plain, hashed)

def password_hash(password):
    return pwd_context.hash(password)

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

@router.post('/register')
def register(request: AuthForm, db: Session = Depends(get_db)):
    try:
        request.password = password_hash(request.password)
        admin = Admin(
            username = request.username,
            password = request.password
        )
        db.add(admin)
        db.commit()
        return {'message': 'Registered Successfully!'}
    except Exception as e:
        print(e)

@router.post('/verify')
def login(form: AuthForm, response: Response, db: Session = Depends(get_db)):
    try:
        admin = db.query(Admin).filter(Admin.username == form.username).first()
        if admin:
            match = password_verify(form.password, admin.password)
            if match:
                data = AuthForm(username = admin.username, password = admin.password)
                token = jwt.encode(dict(data), secret)
                response.set_cookie('token', token, httponly=True)
                return {'message': 'Log In Success!'}
        
        return {'message': 'User not found.'}
    except Exception as e:
        print(e)

@router.post('/logout')
def logout(response: Response):
    response.delete_cookie('token')
    return {'message': 'Logout Success!'}