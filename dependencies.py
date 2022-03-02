from fastapi import Cookie, HTTPException
from jose import jwt, JWTError


secret = '663a6bf88c8c876764cd94e445eacd61154424e1eed23b0d3f0befe08bcd646c'

def get_token(token: str = Cookie('token')):
    try:
        admin = jwt.decode(token, secret)
        if admin:
            return admin
    except JWTError:
        raise HTTPException(401, 'Please Log In first')