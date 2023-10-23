from fastapi import APIRouter
from .database  import engine, SessionLocal, Base
from pydantic import BaseModel
from .user_models import User

user_router = APIRouter()



class UserScheme(BaseModel):
    name: str
    email: str
    password: str
    is_admin: bool

@user_router.get("/getUsers")
def read_users():
    db = SessionLocal()
    Users = db.query(User).all()
    db.close()
    return Users

@user_router.post("/postUsers")
def create_user(user: UserScheme):
    db = SessionLocal()
    db_user = User(name=user.name, email=user.email, password=user.password, is_admin=False)
    
    db.add(db_user)
    db.commit()
    db.close()
    return db_user