sklearn-api-deploy

A quick POC on creating an sklearn model and deploying it via a FastAPI server.

Run the api with:
```
uvicorn api.main:app --host 0.0.0.0 --port 8000
```

## Example Usage
```text
>>> import requests
>>> response = requests.post("http://localhost:8001/prediction", json={"sepal_width": 1, "sepal_length": 1, "petal_length": 1, "petal_width": 1})
>>> response.status_code
200
>>> response.json()
{'flower_type': 0}
```
