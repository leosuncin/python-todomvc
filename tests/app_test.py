from main import app
from fastapi.testclient import TestClient
import pytest


@pytest.fixture
def client():
    return TestClient(app)


def test_greeting(client):
    response = client.get("/greeting")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


@pytest.mark.parametrize("name", ["John", "Jane"])
def test_greeting_name(client, name):
    response = client.get(f"/greeting?name={name}")
    assert response.status_code == 200
    assert response.json() == {"message": f"Hello {name}"}
