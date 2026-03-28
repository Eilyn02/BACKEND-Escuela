"""
Permite capturar excepciones y devolver respuestas.
"""

from fastapi import HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from src.core.exceptions import AppException
from src.core.responses import error_response


async def app_exception_handler(request: Request, exc: AppException):
    """
    Maneja excepciones personalizadas del sistema.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content=error_response(message=exc.message, code=exc.code)
    )


async def http_exception_handler(request: Request, exc: HTTPException):
    """
    Maneja excepciones HTTP estándar de FastAPI.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content=error_response(message=str(exc.detail), code="http_error")
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    Maneja errores de validación de datos.
    """
    return JSONResponse(
        status_code=422,
        content=error_response(
            message="Error de validación en los datos enviados",
            code="validation_error",
            details=exc.errors()
        )
    )


async def generic_exception_handler(request: Request, exc: Exception):
    """
    Maneja errores no controlados del sistema.
    """
    return JSONResponse(
        status_code=500,
        content=error_response(
            message=f"Error interno del servidor: {str(exc)}",
            code="internal_server_error"
        )
    )