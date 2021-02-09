from fastapi.testclient import TestClient

from hsapodaca.src.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}


def test_read_comic():
    response = client.get("/xkcd/100")
    assert response.status_code == 200


def test_read_comic_watercolor():
    response = client.get("/xkcd/100/watercolor")
    assert response.status_code == 200


def test_read_random_comic():
    response = client.get("/xkcd/random")
    assert response.status_code == 200


def test_read_random_comic_watercolor():
    response = client.get("/xkcd/random/watercolor")
    assert response.status_code == 200


def test_read_comic_nonexistent():
    response = client.get("/xkcd/100000000000")
    assert response.status_code == 404
    assert response.json() == {"detail": "Comic not found"}
