import httpx

from src.crud.config import BASE_URL


def obtener_estudiantes():
    response = httpx.get(f"{BASE_URL}/estudiantes/")
    return response.json()


def obtener_estudiante_por_id(id_estudiante):
    response = httpx.get(f"{BASE_URL}/estudiantes/{id_estudiante}")
    return response.json()


def crear_estudiante(nombre, apellido, correo, id_grado):
    data = {
        "nombre": nombre,
        "apellido": apellido,
        "correo": correo,
        "id_grado": id_grado,
    }
    response = httpx.post(f"{BASE_URL}/estudiantes/", json=data)
    return response.json()


def actualizar_estudiante(id_estudiante, nombre, apellido, correo, id_grado):
    data = {
        "nombre": nombre,
        "apellido": apellido,
        "correo": correo,
        "id_grado": id_grado,
    }
    response = httpx.put(f"{BASE_URL}/estudiantes/{id_estudiante}", json=data)
    return response.json()


def eliminar_estudiante(id_estudiante):
    response = httpx.delete(f"{BASE_URL}/estudiantes/{id_estudiante}")
    return response.json()
