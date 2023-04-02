from fastapi.testclient import TestClient


def test_status_endpoint(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200
    payload = response.json()
    assert payload == "the API is up and running!"


def test_predict(client: TestClient):
    response = client.post(
        "/predict",
        json={
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2,
        },
    )
    assert response.status_code == 201
    payload = response.json()
    assert payload["flower_type"] == "setosa"