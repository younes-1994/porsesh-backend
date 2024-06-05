"""Logic for authentication and authorization"""
import os
from dotenv import load_dotenv
from fastapi import HTTPException
from starlette import status
from .schemas import Login

load_dotenv()
USERNAME = os.getenv("FORM_USER")
PASSWORD = os.getenv("FORM_PASS")

def authenticate_user(login: Login):
    """ Method called to authenticate a user.
    :param username: Username
    :param password: Password as plain text
    """
    auth = False
    
    if login.username == USERNAME and login.password == PASSWORD:
        auth = True

    if auth == False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Wrong auth."
        )
    return auth