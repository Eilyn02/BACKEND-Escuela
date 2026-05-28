"""Pruebas de login y endpoints protegidos."""


def get_token(client):
    login = client.post(
        "/auth/login", json={"correo": "admin@escuela.com", "password": "Admin123*"}
    )

    body = login.json()

    return body["access_token"]


def test_login_success(client):
    response = client.post(
        "/auth/login", json={"correo": "admin@escuela.com", "password": "Admin123*"}
    )

    assert response.status_code == 200

    body = response.json()

    assert "access_token" in body


def test_login_invalid_password(client):
    response = client.post(
        "/auth/login", json={"correo": "admin@escuela.com", "password": "incorrecta"}
    )

    assert response.status_code in [400, 401, 404]


def test_get_profesores_with_token(client):
    token = get_token(client)

    response = client.get("/profesores/", headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200


def test_get_estudiantes_with_token(client):
    token = get_token(client)

    response = client.get("/estudiantes/", headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
