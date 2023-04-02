from sklearn.datasets import load_iris
from fastapi.testclient import TestClient

iris = load_iris()
iris_features = iris.data
iris_target = iris.target


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

    response = client.post(
        "/predict",
        json={
            "sepal_length": 7.1,
            "sepal_width": 3.5,
            "petal_length": 3.0,
            "petal_width": 0.8,
        },
    )
    assert response.status_code == 201
    payload = response.json()
    assert payload["flower_type"] == "versicolour"
