from fastapi import Cookie, HTTPException
from jose import jwt, JWTError


secret = 'a very shady secret'

def get_token(token: str = Cookie('token')):
    try:
        user = jwt.decode(token, secret)
        if user:
            return user
    except JWTError:
        raise HTTPException(401, 'Please Log In first')