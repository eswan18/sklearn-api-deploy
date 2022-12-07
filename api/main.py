import pickle
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from fastapi import FastAPI
from .pydantic_models import Observation, Prediction, FlowerType

MODEL_PATH = Path('./models/mymodel.pickle')

def load_model(path: Path) -> GradientBoostingClassifier:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    return model

model = load_model(MODEL_PATH)

app = FastAPI()

@app.get('/')
def home():
    return 'the api is up and running!'

@app.post('/prediction')
def predict(obs: Observation) -> Prediction:
    output_class_array = model.predict(obs.as_dataframe())
    # output_class_array is an array, but has only one element -- the prediction for our record.
    output_class = output_class_array[0]
    flower_type = FlowerType(output_class)
    pred = Prediction(flower_type=flower_type)
    return pred