from datetime import timedelta
from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from crud.user import create_user, get_user_by_email, get_user_by_email_register, validate_email_format, verify_password_sss, get_all_users
from schemas.user import Token, UserBase, UserCreate, UserRegister, UserResponse
from utils.auth import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from database.database import db
from fastapi.responses import JSONResponse
from fastapi import status
from sqlalchemy.orm import Session
from database.database import get_db


router = APIRouter(tags=["auth"])

@router.post("/login", response_model=Token)
def login(db: db, form_data: OAuth2PasswordRequestForm = Depends()):
    # Validacija email formata
    validate_email_format(form_data.username)

    # Pronađi korisnika prema email-u
    user = get_user_by_email(db, email=form_data.username)

    # Ako korisnik nije pronađen, vratiti 401 grešku
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    # Provera lozinke
    is_pwd_verify = verify_password_sss(form_data.password, user.password)

    # Ako lozinka nije tačna, vratiti 401 grešku
    if not is_pwd_verify:
        raise HTTPException(status_code=401, detail="Incorrect password")

    # Generisanje JWT tokena
    access_token = create_access_token(data={"sub": user.email}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
     
    return {"access_token": access_token, "token_type": "bearer", "message": "log in good"}




@router.post("/register", response_model=Token)
def register(db: db, user_data: UserRegister):
    existing_user = get_user_by_email_register(db, email=user_data.email)
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="A user with this email already exists."
        )
    user = create_user(db, user_data)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return {"access_token": access_token, "token_type": "bearer", "message":"registration good"}


'''
@router.get("/allusers", response_model=List[UserResponse])
def read_users (db: Session = Depends(get_db)):
    try:
        users = get_all_users(db)
        return users
    except Exception as e:
        # Ovo ti hvata bilo koju grešku i šalje nazad kao odgovor
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": f"Server error: {str(e)}"}
        )
 '''       