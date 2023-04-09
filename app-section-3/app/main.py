from fastapi import FastAPI
from .pydantic_models import Observation, Prediction


app = FastAPI()


@app.get("/")
def status():
    """Check that the API is working."""
    return "the API is up and running!"


@app.post("/predict", status_code=201)
def predict(obs: Observation) -> Prediction:
    """For now, just return a dummy prediction."""
    return Prediction(flower_type="setosa")
