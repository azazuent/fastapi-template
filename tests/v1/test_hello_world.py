import pytest
from fastapi.testclient import TestClient

from src import app_v1


@pytest.fixture()
def client():
    with TestClient(app=app_v1) as client:
        return client


def test_hello_world(
        client: TestClient
):
    response = client.get("/api/v1/hello_world")

    assert response.status_code == 200
    assert response.json()["message"] == "Hello, World!"
