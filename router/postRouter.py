from fastapi import APIRouter, Request, Depends
from sqlalchemy import or_
from sqlalchemy.orm import Session
from schemas.postSchema import CreatePost
from models.postModel import Post
from models.userModel import User
from database import get_db
from datatables import DataTable

router = APIRouter(
    prefix='/posts',
    tags=['posts']
)

@router.get('/datatable')
def datatable(request: Request, db: Session = Depends(get_db)):
    try:
        def perform_search(queryset, user_input):
            return queryset.filter(
                or_(
                    User.name.like('%' + user_input + '%'),
                    Post.title.like('%' + user_input + '%'),
                    Post.body.like('%' + user_input + '%')
                )
            )

        table = DataTable(dict(request.query_params), Post, db.query(Post), [
            ('author_name', 'author.name'),
            'title',
            'body'
        ])

        table.searchable(lambda queryset, user_input: perform_search(queryset, user_input))
    
        return table.json()
    except Exception as e:
        print(e)


