from database.database import db
from fastapi import APIRouter, Depends, HTTPException, Query, Path
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from models.user import User
from typing import List
from crud.user import get_all_users, get_user_by_id, get_users_by_roles, update_user
from schemas.user import  UserResponse, UserUpdate
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


@router.get("/get_user/{user_id}", response_model=UserResponse)
def get_userbyid(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/get_users_by_roles", response_model=List[UserResponse])
def get_users_by_roles_route(
    role: str = Query(..., title="Role korisnika", description="Role korisnika za filtriranje"),
    db: Session = Depends(get_db)
):
    users = get_users_by_roles(db, role)
    if not users:
        raise HTTPException(status_code=404, detail="Users not found with given role")
    return users

@router.put("/update_user/{user_id}", response_model=UserResponse)
def update_user_route(
    user_id: int,
    user_update: UserUpdate,
    db: Session = Depends(get_db)
):
    updated_user = update_user(db, user_id, user_update)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user




