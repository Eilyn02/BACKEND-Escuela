from fastapi import FastAPI

app = FastAPI(title="API Escuela", version="1.0.0")


@app.get("/")
def home():
    return {"message": "Bienvenido a la API de la Escuela"}
