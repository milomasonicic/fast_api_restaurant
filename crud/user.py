from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.user import User
from schemas.user import UserRegister, UserUpdate
from utils.auth import hash_password, verify_password
from database.database import db
import re

def validate_email_format(email: str):
    email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(email_regex, email):
        raise HTTPException(status_code=400, detail="Invalid email format.")

def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()

def get_user_by_email_register(db: Session, email: str) -> User | None:
    # Možeš koristiti istu funkciju kao i gore, ali ostavljeno odvojeno ako želiš da ih razdvojiš
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user_data: UserRegister) -> User:
    new_user = User(
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        email=user_data.email,
        password=hash_password(user_data.password),
        role=user_data.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def verify_password_sss(plain_password: str, hashed_password: str) -> bool:
    return verify_password(plain_password, hashed_password)


     # Generisanje JWT tokena
    access_token = create_access_token(data={"sub": user.email}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    
    # Vraćanje tokena kao odgovor
    return {"access_token": access_token, "token_type": "bearer"}


# crud/user.py

def get_all_users(db):
    return db.query(User).all()


# def get user by id
def get_user_by_id(db, user_id:int):
    return db.query(User).filter(User.id == user_id).first()

### user by roles
def get_users_by_roles(db, role:str):
    return db.query(User).filter(User.role == role).all()

### user update
# crud.py
def update_user(db, user_id: int, user_update: UserUpdate):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    for field, value in user_update.dict(exclude_unset=True).items():
        setattr(user, field, value)
    db.commit()
    db.refresh(user)
    return user


