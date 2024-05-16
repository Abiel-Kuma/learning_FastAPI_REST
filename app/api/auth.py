from pydantic import BaseModel
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
import bcrypt
from ..models.user_models import User
from ..database.database import SessionLocal


class UserLogin(BaseModel):
    name: str
    password: str


auth_router = APIRouter()


@auth_router.post("/login")
def login(user: UserLogin):
    try:
        # Crear una instancia de la sesión de la base de datos
        db = SessionLocal()

        # Buscar el usuario por nombre en la base de datos
        user_in_db = db.query(User).filter(User.name == user.name).first()

        # Verificar si el usuario existe
        if not user_in_db:
            return JSONResponse(
                content={"message": "Usuario no encontrado"}, status_code=404
            )

        # Verificar la contraseña ingresada por el usuario con la contraseña almacenada
        if bcrypt.checkpw(user.password.encode("utf-8"), user_in_db.password):
            return JSONResponse(
                content={"message": "Inicio de sesión exitoso"}, status_code=200
            )
        else:
            return JSONResponse(
                content={"message": "Contraseña incorrecta"}, status_code=400
            )

    except Exception as e:
        # Manejar la excepción de manera apropiada, por ejemplo, registrando el error
        print("error: " + str(e))
        return JSONResponse(
            content={"message": "Error interno del servidor"}, status_code=500
        )
    finally:
        db.close()
