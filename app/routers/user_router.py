from database import conn_db
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models.user_model import users

conn = conn_db.conn
meta = conn_db.meta

user = APIRouter()

@user.get("/getUser")
def getUser():
    query = conn.execute(user.select(users.select()))
    return JSONResponse(query)
    