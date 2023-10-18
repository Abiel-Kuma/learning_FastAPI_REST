from fastapi import FastAPI

app = FastAPI

@app.get("/")
def index():
    return {"Saludos" : "tratemos de explotar el codigo"}