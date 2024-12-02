import pytest
from fastapi.testclient import TestClient

from ..api import app


@pytest.fixture()
def client():
    with TestClient(app=app) as client:
        return client


def test_hello_world(
        client: TestClient
):
    response = client.get("/api/hello_world")

    assert response.status_code == 200
    assert response.json()["message"] == "Hello, World!"
