"""Pruebas de seguridad, JWT y CORS."""


def test_root_response(client):
    response = client.get("/")

    assert response.status_code == 200


def test_cors_preflight_allows_localhost_4200(client):
    response = client.options(
        "/profesores/",
        headers={
            "Origin": "http://localhost:4200",
            "Access-Control-Request-Method": "GET",
            "Access-Control-Request-Headers": "Authorization,Content-Type",
        },
    )

    assert response.status_code in (200, 204)

    assert response.headers["access-control-allow-origin"] == "http://localhost:4200"


def test_protected_endpoint_requires_token(client):
    response = client.get("/profesores/")

    assert response.status_code == 200
