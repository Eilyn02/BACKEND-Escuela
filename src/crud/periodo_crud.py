import httpx

from src.crud.config import BASE_URL


def obtener_periodos():
    response = httpx.get(f"{BASE_URL}/periodos/")
    return response.json()


def obtener_periodo_por_id(id_periodo):
    response = httpx.get(f"{BASE_URL}/periodos/{id_periodo}")
    return response.json()


def crear_periodo(nombre, fecha_inicio, fecha_fin):
    data = {"nombre": nombre, "fecha_inicio": fecha_inicio, "fecha_fin": fecha_fin}
    response = httpx.post(f"{BASE_URL}/periodos/", json=data)
    return response.json()


def actualizar_periodo(id_periodo, nombre, fecha_inicio, fecha_fin):
    data = {"nombre": nombre, "fecha_inicio": fecha_inicio, "fecha_fin": fecha_fin}
    response = httpx.put(f"{BASE_URL}/periodos/{id_periodo}", json=data)
    return response.json()


def eliminar_periodo(id_periodo):
    response = httpx.delete(f"{BASE_URL}/periodos/{id_periodo}")
    return response.json()
