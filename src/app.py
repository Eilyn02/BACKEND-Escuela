"""
Aplicación FastAPI. Ejecutar con:
  uvicorn src.app:app --reload --host 0.0.0.0 --port 8000
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.database.config import create_tables

# Importar modelos para que Base.metadata los conozca
import src.entities.profesor  # noqa: F401
import src.entities.estudiante  # noqa: F401
import src.entities.materia  # noqa: F401
import src.entities.periodo  # noqa: F401
import src.entities.grado  # noqa: F401
import src.entities.nota  # noqa: F401


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield


app = FastAPI(
    title="API Escuela",
    description="API con FastAPI, SQLAlchemy y PostgreSQL para la gestión de una escuela",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/")
def inicio():
    return {"mensaje": "API Escuela", "docs": "/docs"}
