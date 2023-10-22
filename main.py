from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database  import engine, SessionLocal, Base
from app.models import User
# cositas
from pydantic import BaseModel

class UserScheme(BaseModel):
    name: str
    email: str
    password: str
    is_admin: bool

app = FastAPI() 
# Configurar CORS para permitir solicitudes desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes ajustar esta lista según tus necesidades
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Agregar esta función para crear la tabla
def create_tables():
    Base.metadata.create_all(bind=engine)

# Rutas y operaciones de la API que utilizan la base de datos
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/getUsers")
def read_users():
    db = SessionLocal()
    Users = db.query(User).all()
    db.close()
    return Users

@app.post("/postUsers")
def create_user(user: UserScheme):
    db = SessionLocal()
    db_user = User(name=user.name, email=user.email, password=user.password, is_admin=False)
    
    db.add(db_user)
    db.commit()
    db.close()
    return db_user

if __name__ == "__main__":
    create_tables()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
