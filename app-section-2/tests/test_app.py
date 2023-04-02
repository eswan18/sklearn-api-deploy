from fastapi.testclient import TestClient


def test_status_endpoint(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200
    payload = response.json()
    assert payload == "the API is up and running!"
