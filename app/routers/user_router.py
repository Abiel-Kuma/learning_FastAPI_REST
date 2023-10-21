from fastapi import APIRouter
from fastapi.responses import JSONResponse

user = APIRouter()
#rutas
@user.get("/getUser")
def getUser():
    return JSONResponse()