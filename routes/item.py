"""from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from fastapi import HTTPException
from models.user import User
from schemas.user import UserBase, UserResponse
from core.database import get_db
from crud.user import create_user, get_all_users, get_user_by_id, delete_user, update_user

router = APIRouter()"""

'''
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from models.item import Item
from crud.item import create_item
from schemas.item import ItemBase, ItemResponse
from database.database import get_db

router = APIRouter()

@router.post("/createItem/", response_model= ItemResponse)
async def create_item(item: ItemBase, db: Session = Depends(get_db)):
    new_item = create_item(item, db)
    return ItemResponse(message="Item created successfully!")

    '''