# app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os
from typing import List
from app.schemas import HeartFeatures

app = FastAPI(title="Heart Disease Prediction API")

MODEL_PATH = os.environ.get("MODEL_PATH", "model/heart_model.joblib")

# Load model at startup
model_bundle = None
FEATURES = []
MODEL_TYPE = "unknown"

@app.on_event("startup")
def load_model():
    global model_bundle, FEATURES, MODEL_TYPE
    if not os.path.exists(MODEL_PATH):
        raise RuntimeError(f"Model file not found at {MODEL_PATH}. Please train and place it there.")
    model_bundle = joblib.load(MODEL_PATH)
    # model_bundle is dict with keys: model, features, model_type
    FEATURES = model_bundle.get("features", [])
    MODEL_TYPE = model_bundle.get("model_type", "unknown")
    print("Model loaded. Features:", FEATURES)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/info")
def info():
    return {
        "model_type": MODEL_TYPE,
        "features": FEATURES
    }

@app.post("/predict")
def predict(data: HeartFeatures):
    # Convert input to model-ready array in correct order
    try:
        features = [getattr(data, f) for f in FEATURES]
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Bad input: {e}")

    model = model_bundle["model"]
    pred = model.predict([features])[0]
    prob = None
    # if classifier supports predict_proba
    if hasattr(model, "predict_proba"):
        prob = model.predict_proba([features])[0].tolist()

    return {
        "heart_disease": bool(int(pred)),
        "probabilities": prob
    }
