from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
import jwt
from ..models.user_models import User
from ..database.database import SessionLocal

password_context = CryptContext(schemes=["sha256_crypt"])

# todo: agregar la doble autenticacion con JWT
class Token(BaseModel):
    access_token: str
    token_type: str

# todo: agregar .env a esto
SECRET_KEY = "tu_secreto"
ALGORITHM = "HS256"



auth_router = APIRouter()

@auth_router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        # Crear una instancia de la sesión de la base de datos
        db = SessionLocal()

        # Buscar el usuario por nombre en la base de datos
        user_in_db = db.query(User).filter(User.name == form_data.username).first()

        # Verificar si el usuario existe
        if not user_in_db:
            return JSONResponse(status_code=404, content={"detail": "Usuario no encontrado"})

        # Verificar contraseña
        if not password_context.verify(form_data.password, user_in_db.password):
            return JSONResponse(status_code=400, content={"detail": "Contraseña incorrecta"})


        # generar token
        token_data = {"sub": form_data.username}
        access_token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)

        # retornamos el token
        return Token(access_token=access_token, token_type="bearer")

    except Exception as e:
        # Manejar excepción
        print("error: " + str(e))
        raise HTTPException(status_code=500, detail="Error interno del servidor")

    finally:
        db.close()
