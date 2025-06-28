from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.item import Item
from schemas.item import ItemBase
from utils.auth import hash_password, verify_password
from database.database import db
import re


def create_item(item: ItemBase, db: Session):
    new_item = Item(
        name=item.name,
        price=item.price,
        descritpion=item.descritpion,
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    ###return new_item