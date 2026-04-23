from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Depends
from sqlalchemy.orm import Session

# Database Set Up
from model_loader import sentiment_pipeline
from database import engine
from models import Base
from database import get_db
from models import Prediction

# Create tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Request body schema
class PredictRequest(BaseModel):
    text: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/predictions")
def get_predictions(db: Session = Depends(get_db)):
    predictions = db.query(Prediction).order_by(Prediction.id.desc()).limit(50).all() 
    return [
        {
            "id": p.id,
            "text": p.text,
            "label": p.label,
            "score": p.score,
            "created_at": p.created_at
        }
        for p in predictions
    ]

@app.post("/predict")
def predict(request: PredictRequest, db: Session = Depends(get_db)):
    result = sentiment_pipeline(request.text)[0]
    # Create database row 
    prediction = Prediction(
        text=request.text,
        label=result["label"],
        score=result["score"]
    )
    # Save and write row to Postgres
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    return {
        "label": result["label"],
        "score": result["score"]
    }