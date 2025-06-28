from pydantic import BaseModel, EmailStr, validator
from models.user import UserRole
from typing import Optional


# Za registraciju korisnika
class UserRegister(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    role: UserRole = UserRole.buyer

    @validator('password')
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return value

    class Config:
        orm_mode = True


# Za kreiranje korisnika iz admin panela (npr.)
class UserCreate(UserRegister):
    pass  # koristi sve isto kao UserRegister


# Baza korisnika bez lozinke
class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    role: UserRole

    class Config:
        orm_mode = True


# Za prikaz korisnika
class UserResponse(UserBase):
    id: int
    first_name:str
    last_name:str
    email:str
    password:str
    role:UserRole
    password:str


# Za login token
class Token(BaseModel):
    access_token: str
    token_type: str
    message: str