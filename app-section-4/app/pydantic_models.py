from typing import Literal

import pandas as pd
from pydantic import BaseModel


class Observation(BaseModel):
    """An observation of a flower's measurements."""
    # For later parts of this code to work, the order of fields here needs to match the
    # order they were listed in training.
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    def as_dataframe(self) -> pd.DataFrame:
        """Convert this record to a DataFrame with one row."""
        return pd.DataFrame([self.as_row()])

    def as_row(self) -> pd.Series:
        # Note: the order here is vital; if these aren't in the same order as they were in training, sklearn will complain.
        values = (
            self.sepal_length,
            self.sepal_width,
            self.petal_length,
            self.petal_width,
        )
        colnames = (
            "sepal length (cm)",
            "sepal width (cm)",
            "petal length (cm)",
            "petal width (cm)",
        )
        return pd.Series(values, index=colnames)


class Prediction(BaseModel):
    """A prediction of the species of a flower."""
    flower_type: Literal["setosa", "versicolor", "virginica"]
