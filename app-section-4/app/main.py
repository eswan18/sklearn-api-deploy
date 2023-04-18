import pickle
import importlib
from typing import List

import pandas as pd
from sklearn.linear_model import LogisticRegression
from fastapi import FastAPI
from .pydantic_models import Observation, Prediction


def load_model(model_name: str) -> LogisticRegression:
    with importlib.resources.open_binary("app.models", model_name) as f:
        model = pickle.load(f)
    return model


MODEL_NAME = "iris_regression.pickle"
CLASS_FLOWER_MAPPING = {
    0: 'setosa',
    1: 'versicolor',
    2: 'virginica',
}
model = load_model(MODEL_NAME)
app = FastAPI()


@app.get("/")
def status():
    """Check that the API is working."""
    return "the API is up and running!"


@app.post("/predict", status_code=201)
def predict(obs: Observation) -> Prediction:
    """For now, just return a dummy prediction."""
    # .predict() gives us an array, but it has only one element
    prediction = model.predict(obs.as_dataframe())[0]
    flower_type = CLASS_FLOWER_MAPPING[prediction]
    pred = Prediction(flower_type=flower_type)
    return pred


@app.post("/batch_predict", status_code=201)
def batch_predict(batch: List[Observation]) -> List[Prediction]:
    """Predict the flower type for a batch of observations."""
    rows = [obs.as_row() for obs in batch]
    df = pd.DataFrame(rows)
    output_classes = model.predict(df)
    preds = [
        Prediction(flower_type=CLASS_FLOWER_MAPPING[output_class])
        for output_class in output_classes
    ]
    return preds
