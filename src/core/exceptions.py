"""
Este archivo define errores propios de la aplicación.
"""


class AppException(Exception):
    """
    Excepción base del sistema.
    """

    def __init__(self, message: str, status_code: int = 400, code: str = "app_error"):
        self.message = message
        self.status_code = status_code
        self.code = code
        super().__init__(message)


class NotFoundError(AppException):
    """
    Error para recursos que no existen.
    """

    def __init__(self, message: str = "Recurso no encontrado"):
        super().__init__(message=message, status_code=404, code="not_found")


class ConflictError(AppException):
    """
    Error para conflictos de información, por ejemplo correos repetidos.
    """

    def __init__(self, message: str = "Conflicto de datos"):
        super().__init__(message=message, status_code=409, code="conflict")


class BadRequestError(AppException):
    """
    Error para solicitudes inválidas enviadas por el cliente.
    """

    def __init__(self, message: str = "Solicitud inválida"):
        super().__init__(message=message, status_code=400, code="bad_request")