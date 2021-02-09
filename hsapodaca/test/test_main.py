from fastapi.testclient import TestClient

from hsapodaca.src.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}