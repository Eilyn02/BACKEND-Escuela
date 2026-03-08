"""
Cliente HTTP para consumir los endpoints de profesores.

Utiliza la librería httpx para enviar solicitudes
a la API FastAPI desde el menú por consola.
"""

import httpx

from src.crud.config import BASE_URL


def obtener_profesores():
    response = httpx.get(f"{BASE_URL}/profesores/")
    return response.json()


def obtener_profesor_por_id(id_profesor):
    response = httpx.get(f"{BASE_URL}/profesores/{id_profesor}")
    return response.json()


def crear_profesor(nombre, apellido, correo, especialidad):
    data = {
        "nombre": nombre,
        "apellido": apellido,
        "correo": correo,
        "especialidad": especialidad,
    }
    response = httpx.post(f"{BASE_URL}/profesores/", json=data)
    return response.json()


def actualizar_profesor(id_profesor, nombre, apellido, correo, especialidad):
    data = {
        "nombre": nombre,
        "apellido": apellido,
        "correo": correo,
        "especialidad": especialidad,
    }
    response = httpx.put(f"{BASE_URL}/profesores/{id_profesor}", json=data)
    return response.json()


def eliminar_profesor(id_profesor):
    response = httpx.delete(f"{BASE_URL}/profesores/{id_profesor}")
    return response.json()
