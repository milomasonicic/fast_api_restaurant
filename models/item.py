from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from passlib.context import CryptContext
from enum import Enum as PyEnum
from database.database import Base 


class Item(Base):
    __tablename__="items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    descritpion = Column(String, nullable=False)
    price =  Column(Integer, nullable=False)
    images = relationship("Image", back_populates="item", cascade="all, delete-orphan")  