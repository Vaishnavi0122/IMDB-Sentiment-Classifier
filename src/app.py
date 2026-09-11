from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI(title="IMDB Sentiment Classifier")

# Load the trained model
model = joblib.load("../models/imdb_sentiment_model.pkl")


class ReviewRequest(BaseModel):
    review: str


@app.get("/")
def home():
    return {"message": "IMDB Sentiment Classifier API is running!"}


@app.post("/predict")
def predict_sentiment(request: ReviewRequest):
    prediction = model.predict([request.review])[0]
    probabilities = model.predict_proba([request.review])[0]

    confidence = max(probabilities) * 100

    return {
        "sentiment": prediction,
        "confidence": round(confidence, 2)
    }