from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from passlib.context import CryptContext
from enum import Enum as PyEnum
from database.database import Base 
# Enum za definisanje uloga korisnika
class UserRole(PyEnum):
    admin = "admin"
    stuff = "stuff"
    buyer = "buyer"

class User(Base):
    __tablename__ = "users"

    # Id je primarni ključ
    id = Column(Integer, primary_key=True, index=True)
    
    # Kolone koje sadrže ime, prezime, email, lozinku i ulogu
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)  # Šifrovana lozinka
    role = Column(Enum(UserRole), default=UserRole.buyer, nullable=False)

    # Dodatna veza sa drugim tabelama može biti postavljena ovde, ako je potrebno.
