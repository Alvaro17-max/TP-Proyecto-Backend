import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client

def test_get_deportes(client):
    response = client.get("/deportes")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_post_socio_invalido_faltan_campos(client):
    response = client.post("/socios", json={"nombre": "Solo Nombre"})
    assert response.status_code == 400
    assert "error" in response.get_json()

def test_post_reserva_cancha_inexistente(client):
    datos = {
        "id_socio": 1,
        "id_cancha": 9999,
        "fecha_hora_inicio": "2026-12-01 10:00:00",
        "fecha_hora_fin": "2026-12-01 12:00:00"
    }
    response = client.post("/reservas", json=datos)
    assert response.status_code in (400, 404)