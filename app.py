from fastapi import FastAPI
from database.database import Base, engine
from routes import auth, item, users

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(users.router)
####app.include_router(item.router) 

@app.get("/")
def read_root():
    return "Hello milo"
