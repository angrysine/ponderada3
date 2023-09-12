# -*- coding: utf-8 -*-

import pandas as pd
from pycaret.regression import load_model, predict_model
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

# Create the app
app = FastAPI()

# Load trained Pipeline
model = load_model("teste_api")

# Create input/output pydantic models
class input_model(BaseModel):
    CustomerID: int
    Gender: int
    Age: int
    Income: int



@app.get("/")
def home():
    return "API is working!"

# Define predict function
@app.post("/predict")
def predict(data: input_model):
    data = pd.DataFrame([data.dict()])
    predictions = predict_model(model, data=data)
    return {"prediction": predictions["prediction_label"].iloc[0]}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
