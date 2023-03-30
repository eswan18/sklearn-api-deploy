# sklearn-api-deploy

A quick POC of deploying an sklearn model in a FastAPI server.

# The Model

You can download the trained model pickle file from [here](https://www.dropbox.com/s/q0iek2hu43oz3c0/iris_regression.pickle?dl=0).

If you want to verify it's the file you expect before unpickling it, run:
```bash
md5 iris_regression.pickle
```
You should get an md5 hash of `ca76ff2631132e4ec5841a2b798534ca`.

## Running the API Server

Start the api with:
```
uvicorn api.main:app --host 0.0.0.0 --port 8000
```

## Fetching Predictions

If the API server is running at `http://localhost:8000`, then the following should work in a local Python session:
```text
>>> import requests
>>> response = requests.post("http://localhost:8000/prediction", json={"sepal_width": 1, "sepal_length": 1, "petal_length": 1, "petal_width": 1})
>>> response.status_code
200
>>> response.json()
{'flower_type': 0}
```
