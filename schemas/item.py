# schemas/item.py
from pydantic import BaseModel
from typing import Literal

class ItemBase(BaseModel):
    name: str
    price: int
    descritpion: str  # ispraviti 'descritpion' u 'description' ako je potrebno

class ItemResponse(BaseModel):
    message: str
   

class Config:
        orm_mode = True


