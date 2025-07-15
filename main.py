from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import joblib

# Initialize the FastAPI app
app = FastAPI()

# Load the trained models
xgb_model = joblib.load("xgb_model.pkl")
embed_model = SentenceTransformer("embed_model")

# Define input schema
class NewsText(BaseModel):
    text: str

# Prediction endpoint
@app.post("/predict")
def predict(news: NewsText):
    # Convert input to embedding
    embedding = embed_model.encode([news.text])
    # Predict with XGBoost model
    prediction = xgb_model.predict(embedding)[0]
    # Return human-readable result
    result = "🟢 Real News" if prediction == 1 else "🔴 Fake News"
    return {"prediction": result}

# Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve HTML at root URL
@app.get("/")
def serve_html():
    return FileResponse(os.path.join("static", "fake_news_detector_chat.html"))

from fastapi import Request
from datetime import datetime

class Feedback(BaseModel):
    type: str
    comment: str | None = None
    timestamp: str
    user_input: str | None = None  # Optional original text for context

@app.post("/feedback")
def receive_feedback(feedback: Feedback, request: Request):
    # Log or save feedback
    with open("feedback_log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{feedback.timestamp}] Feedback: {feedback.type}\n")
        if feedback.comment:
            f.write(f"Comment: {feedback.comment}\n")
        if feedback.user_input:
            f.write(f"User Input: {feedback.user_input}\n")
        f.write("-" * 40 + "\n")
    return {"status": "success", "message": "Feedback received"}
