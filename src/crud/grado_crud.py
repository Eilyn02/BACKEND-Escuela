import httpx

from src.crud.config import BASE_URL


def obtener_grados():
    response = httpx.get(f"{BASE_URL}/grados/")
    return response.json()


def obtener_grado_por_id(id_grado):
    response = httpx.get(f"{BASE_URL}/grados/{id_grado}")
    return response.json()


def crear_grado(nombre):
    data = {"nombre": nombre}
    response = httpx.post(f"{BASE_URL}/grados/", json=data)
    return response.json()


def actualizar_grado(id_grado, nombre):
    data = {"nombre": nombre}
    response = httpx.put(f"{BASE_URL}/grados/{id_grado}", json=data)
    return response.json()


def eliminar_grado(id_grado):
    response = httpx.delete(f"{BASE_URL}/grados/{id_grado}")
    return response.json()
