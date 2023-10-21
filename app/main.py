from fastapi import FastAPI
from app.routers.user_router import user

app = FastAPI()

@app.get("/")
def index():
    return {"mensaje": "Saludos, tratemos de explotar el código"}

app.include_router(user)