# Iris Prediction API

This repo contains an Iris prediction server.
To start the application, run:
```
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Fetching Predictions

If the API server is running at `http://localhost:8000`, then the following should work in a local Python session:
```text
>>> import requests
>>> response = requests.post(
...     "http://localhost:8000/predict",
...     json={
...         "sepal_width": 1,
...         "sepal_length": 1,
...         "petal_length": 1,
...         "petal_width": 1,
...     },
... )
>>> response.status_code
200
>>> response.json()
{'flower_type': 0}
```
