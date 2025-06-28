from database.database import db
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from models.user import User
from typing import List
from crud.user import get_all_users
from schemas.user import  UserResponse
from database.database import get_db

'''
@router.get("/allusers", response_model=List[UserResponse])
def read_users(db: Session = Depends(get_db)):
    users = get_all_users(db)
    return users
'''

router = APIRouter(tags=["auth"])

@router.get("/allusers", response_model= List[UserResponse])
def read_users(db: Session = Depends(get_db)):
    users = get_all_users(db)
    return users    

