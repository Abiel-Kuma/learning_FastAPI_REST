from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from app.database.database import engine, Base, SessionLocal
from app.api.user import user_router
from app.api.auth import auth_router

app = FastAPI() 

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(user_router)
app.include_router(auth_router)

#inicia el servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000) 