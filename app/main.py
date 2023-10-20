from fastapi import FastAPI
from routers.user_router import user
app = FastAPI()

@app.get("/")
def index():
    return {"Saludos" : "tratemos de explotar el codigo"}

app.include_router(user)