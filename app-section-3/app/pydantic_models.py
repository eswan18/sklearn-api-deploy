from typing import Literal

from pydantic import BaseModel


class Observation(BaseModel):
    # For later parts of this code to work, the order of fields here needs to match the
    # order they were listed in training.
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


class Prediction(BaseModel):
    flower_type: Literal["setosa", "versicolour", "virginica"]
