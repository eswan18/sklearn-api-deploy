# sklearn-api-deploy

Code examples for my PyCon tutorial, [*Building a Model Prediction Server*](https://us.pycon.org/2023/schedule/presentation/79/).
Slides for that tutorial are [here](https://eswan18.github.io/sklearn-api-deploy-slides/sklearn-api-deploy.slides.html#/).

## How This Repo Is Organized

The tutorial is divided into four sections, and the code that we'll write in each section is captured in the corresponding `app-section-N` folder.
That is, `app-section-2` contains the state of the project after we've finished sections 1 and 2 of the tutorial.

Additionally, to make it easier to see what changes are made between each step, there are HTML files in the `diffs/` folder to illustrate the differences between each section. `diffs/1.html` shows the code we add in section 1, etc.

## The Dataset

We're using the Iris dataset, a very common example in data science.
Our goal is to create a model to predict the type of flower based on the measurements of its petals and sepals.

This turns out to be very easy, but I chose this dataset because:
1. It has relatively few features. Our goal here is to see how to deploy a model behind an API -- and having many features, while more realistic, just means more code to write without any additional educational value.
2. It doesn't require feature engineering. Again, this is a little bit unrealistic, but allows us to avoid writing code that's unrelated to the model deployment process.

I may include a more complex example in the future, for reference purposes.

## The Model

I've pretrained a linear regression model and stored it in Dropbox.

You can download it with [this link](https://www.dropbox.com/s/q0iek2hu43oz3c0/iris_regression.pickle?dl=0).
If you want to verify its hash, to make sure it's the file you expect before unpickling it, run:
```bash
md5 iris_regression.pickle
```
You should get an md5 hash of `ca76ff2631132e4ec5841a2b798534ca`.

You can see how this model was trained in the `notebooks/train_model.ipynb` notebook.
There's nothing interesting in there and it's not meant to follow best practice; it's just a quick and dirty way to get a model we can use in our API.

## Running the server

We deploy the model via a FastAPI server.
Before we can run it, we need to install our "app" package that contains all the source code for our API.

```bash
cd app-section-4
# Create and empty venv
python3 -m venv venv
# Activate the new venv
source venv/bin/activate  # or `.\venv\Scripts\activate` on windows
# Install our package and its dependencies
pip install -e .
```

Then to start the application, just run:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Note that you'll need to be in a directory that has an `api` folder, so if you're using this repo you'll need to enter one of the subfolders first (e.g. `app-section-4`).

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

## Poetry and `setup.cfg`

I initially set up this full repository with Poetry, since it's what I use for application development, but each individual `app-section-N` folder is set up to be installed as a package with its own dependencies (`pip install -e .`) using a `setup.cfg` file.
To dump the poetry requirements, you can run `poetry export --without-hashes --format=requirements.txt` but a little bit of format-massaging is required to get them in the right form for `setup.cfg`.
