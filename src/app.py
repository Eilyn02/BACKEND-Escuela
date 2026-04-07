"""
Aplicación FastAPI. Ejecutar con:
  uvicorn src.app:app --reload --host 0.0.0.0 --port 8000
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

from src.core.error_handlers import (
    app_exception_handler,
    generic_exception_handler,
    http_exception_handler,
    validation_exception_handler,
)
from src.core.exceptions import AppException

from src.database.config import create_tables
from src.endpoints.estudiante_router import router as estudiante_router
from src.endpoints.grado_router import router as grado_router
from src.endpoints.materia_router import router as materia_router
from src.endpoints.nota_router import router as nota_router
from src.endpoints.periodo_router import router as periodo_router
from src.endpoints.profesor_router import router as profesor_router
from src.endpoints.auth_router import router as auth_router


# Importar modelos para que Base.metadata los conozca
import src.entities.profesor  # noqa: F401
import src.entities.estudiante  # noqa: F401
import src.entities.materia  # noqa: F401
import src.entities.periodo  # noqa: F401
import src.entities.grado  # noqa: F401
import src.entities.nota  # noqa: F401
import src.entities.usuario  # noqa: F401


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

# Configuración de CORS para permitir consumo desde frontend local
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5500",
    "http://localhost:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar manejadores globales de errores
app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

# registrar routers
app.include_router(profesor_router)
app.include_router(estudiante_router)
app.include_router(materia_router)
app.include_router(periodo_router)
app.include_router(grado_router)
app.include_router(nota_router)
app.include_router(auth_router)


@app.get("/")
def inicio():
    return {"success": True, "message": "API Escuela", "data": {"docs": "/docs"}}
