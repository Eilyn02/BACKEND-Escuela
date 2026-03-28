"""
Este archivo permite devolver respuestas con una estructura
uniforme tanto para éxitos como para errores.
"""


def success_response(data=None, message="Operación exitosa"):
    """
    Construye una respuesta exitosa.
    """
    return {
        "success": True,
        "message": message,
        "data": data
    }


def error_response(message="Ha ocurrido un error", code="app_error", details=None):
    """
    Construye una respuesta de error.
    """
    return {
        "success": False,
        "error": {
            "code": code,
            "message": message,
            "details": details
        }
    }