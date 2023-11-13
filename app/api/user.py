from fastapi import APIRouter
from fastapi.responses import JSONResponse
from passlib.context import CryptContext
from ..database.database import engine, SessionLocal, Base
from ..models.user_models import User
from ..schemas.user_schema import UserScheme

password_context = CryptContext(schemes=["sha256_crypt"])

user_router = APIRouter()


@user_router.get("/getUsers")
def read_users():
    db = SessionLocal()
    Users = db.query(User).all()
    db.close()
    return Users


@user_router.post("/postUsers")
def create_user(user: UserScheme):
    user.password = password_context.hash(user.password)
    db = SessionLocal()
    db_user = User(
        name=user.name, email=user.email, password=user.password, is_admin=False
    )

    db.add(db_user)
    db.commit()
    db.close()
    return JSONResponse(
        content={"message": "usuario creado exitosamente."}, status_code=201
    )

# todo: restablecer contraseña
@user_router.post("/restPass")
def restPass():
    pass