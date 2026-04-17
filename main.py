from fastapi import FastAPI
from pydantic import BaseModel

from model_loader import sentiment_pipeline

app = FastAPI()


# Request body schema
class PredictRequest(BaseModel):
    text: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(request: PredictRequest):
    result = sentiment_pipeline(request.text)[0]

    return {
        "label": result["label"],
        "score": result["score"]
    }