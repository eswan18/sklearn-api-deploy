# sklearn-api-deploy

A quick POC of deploying a scikit-learn model with a FastAPI server.

## The Dataset

We're using the Iris dataset, a very common example in data science.
Our goal is to create a model to predict the type of flower based on the measurements of its petals and sepals.

This turns out to be very easy, but I chose this dataset because:
- It has relatively few features. Our goal here is to see how to deploy a model behind an API -- and having many features, while more realistic, just means more code to write without any additional educational value.
- It doesn't require feature engineering. Again, this is probably a little bit unrealstic, but allows us to avoid writing code that's unrelated to the model deployment process.

## The Model

I've pretrained a linear regression model and stored it in Dropbox.

You can download it with [this link](https://www.dropbox.com/s/q0iek2hu43oz3c0/iris_regression.pickle?dl=0).
If you want to verify its hash, to make sure it's the file you expect, before unpickling it, run:
```bash
md5 iris_regression.pickle
```
You should get an md5 hash of `ca76ff2631132e4ec5841a2b798534ca`.

You can see how this model was trained in the `notebooks/train_model.ipynb` notebook.

## The API

We deploy the model via a FastAPI server.
To get start the application, run:
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
