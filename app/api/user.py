from fastapi import APIRouter
from fastapi.responses import JSONResponse
import bcrypt
from ..database.database  import engine, SessionLocal, Base
from ..models.user_models import User
from ..schemas.user_schema import UserScheme

user_router = APIRouter()

@user_router.get("/getUsers")
def read_users():
    db = SessionLocal()
    Users = db.query(User).all()
    db.close()
    return Users

@user_router.post("/postUsers")
def create_user(user: UserScheme):
    user.password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt(8))
    db = SessionLocal()
    db_user = User(name=user.name, email=user.email, password=user.password, is_admin=False)
    
    db.add(db_user)
    db.commit()
    db.close()
    return JSONResponse(content={"message" : "usuario creado exitosamente."} , status_code=201)