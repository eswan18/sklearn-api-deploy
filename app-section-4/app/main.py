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
model = load_model(MODEL_NAME)
app = FastAPI()


@app.get("/")
def status():
    """Check that the API is working."""
    return "the API is up and running!"


@app.post("/predict", status_code=201)
def predict(obs: Observation) -> Prediction:
    """Predict the flower type from the given observation."""
    output_class_array = model.predict(obs.as_dataframe())
    print(output_class_array)
    # output_class_array is an array, but has only one element -- the prediction for our record.
    output_class = output_class_array[0]
    flower_type = flower_type_from_class_num(output_class)
    pred = Prediction(flower_type=flower_type)
    return pred


@app.post("/batch_predict", status_code=201)
def batch_predict(batch: List[Observation]) -> List[Prediction]:
    """Predict the flower type for a batch of observations."""
    rows = [obs.as_row() for obs in batch]
    df = pd.DataFrame(rows)
    output_classes = model.predict(df)
    preds = [
        Prediction(flower_type=flower_type_from_class_num(output_class))
        for output_class in output_classes
    ]
    return preds


def flower_type_from_class_num(class_num: int) -> str:
    """Convert the class number to a flower type."""
    if class_num == 0:
        return "setosa"
    elif class_num == 1:
        return "versicolour"
    elif class_num == 2:
        return "virginica"
    else:
        raise ValueError(f"Unknown class number: {class_num}")
