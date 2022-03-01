from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from router import authRouter, userRouter
from database import get_db
from models.postModel import Post

# Register template folder
template = Jinja2Templates('templates')

app = FastAPI()

# Register Routes
app.include_router(authRouter.router)
app.include_router(userRouter.router)

@app.get('/', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    try:
        posts = db.query(Post).all()
        return template.TemplateResponse('index.html', {
            'request': request,
            'posts': posts
        })
    except Exception as e:
        print(e)


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
