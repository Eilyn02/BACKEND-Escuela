import httpx

from src.crud.config import BASE_URL


def obtener_notas():
    response = httpx.get(f"{BASE_URL}/notas/")
    return response.json()


def obtener_nota_por_id(id_nota):
    response = httpx.get(f"{BASE_URL}/notas/{id_nota}")
    return response.json()


def crear_nota(clasificacion, id_estudiante, id_profesor, id_materia, id_periodo):
    data = {
        "clasificacion": clasificacion,
        "id_estudiante": id_estudiante,
        "id_profesor": id_profesor,
        "id_materia": id_materia,
        "id_periodo": id_periodo,
    }
    response = httpx.post(f"{BASE_URL}/notas/", json=data)
    return response.json()


def actualizar_nota(
    id_nota, clasificacion, id_estudiante, id_profesor, id_materia, id_periodo
):
    data = {
        "clasificacion": clasificacion,
        "id_estudiante": id_estudiante,
        "id_profesor": id_profesor,
        "id_materia": id_materia,
        "id_periodo": id_periodo,
    }
    response = httpx.put(f"{BASE_URL}/notas/{id_nota}", json=data)
    return response.json()


def eliminar_nota(id_nota):
    response = httpx.delete(f"{BASE_URL}/notas/{id_nota}")
    return response.json()
