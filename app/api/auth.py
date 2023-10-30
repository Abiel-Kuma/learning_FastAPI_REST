from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
import bcrypt
from ..schemas.user_schema import UserScheme
from ..database.database import SessionLocal

auth = APIRouter()


@auth.post("/login")
def login(user = UserScheme):
    db = SessionLocal()
    user_in_db = db.query(users).filter(name == user.name).first()
    
    if not user_in_db:
        return JSONResponse(content={"message": "Usuario no encontrado"} , status_code=404)

    
     # Verifica la contraseña ingresada por el usuario con la contraseña almacenada
    if not bcrypt.checkpw(user.password.encode('utf-8'), user_in_db.password.encode('utf-8')):
        db.close()
        return JSONResponse(status_code=400, detail="Contraseña incorrecta")

    db.close()