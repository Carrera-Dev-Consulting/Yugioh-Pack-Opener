import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def fastapi_test_client():
    from app.entrypoint.fastapi_app import app

    return TestClient(app)


def test_items(fastapi_test_client: TestClient):
    response = fastapi_test_client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"o": "k"}
