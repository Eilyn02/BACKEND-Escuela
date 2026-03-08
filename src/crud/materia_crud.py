import httpx

from src.crud.config import BASE_URL


def obtener_materias():
    response = httpx.get(f"{BASE_URL}/materias/")
    return response.json()


def obtener_materia_por_id(id_materia):
    response = httpx.get(f"{BASE_URL}/materias/{id_materia}")
    return response.json()


def crear_materia(nombre, id_profesor):
    data = {"nombre": nombre, "id_profesor": id_profesor}
    response = httpx.post(f"{BASE_URL}/materias/", json=data)
    return response.json()


def actualizar_materia(id_materia, nombre, id_profesor):
    data = {"nombre": nombre, "id_profesor": id_profesor}
    response = httpx.put(f"{BASE_URL}/materias/{id_materia}", json=data)
    return response.json()


def eliminar_materia(id_materia):
    response = httpx.delete(f"{BASE_URL}/materias/{id_materia}")
    return response.json()
