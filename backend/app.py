from fastapi import FastAPI, HTTPException
from pathlib import Path
import json

from backend.modeling.predict import predict_aqi
from backend.llm.gemini_explainer import generate_explanation
from backend.utils.config import FEATURE_COLUMNS, BASE_DIR

app = FastAPI(
    title="Lucknow Air Quality Prediction API",
    description="ML-based PM2.5 prediction with Gemini-powered explainability",
    version="1.0"
)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # OK for local + college project
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ------------------------
# Health Check
# ------------------------
@app.get("/")
def health_check():
    return {"status": "API is running"}


# ------------------------
# ML Prediction Endpoint
# ------------------------
@app.post("/predict")
def predict_pm25(data: dict):
    """
    Predict PM2.5 concentration using ML model.
    """
    try:
        pm25_pred = predict_aqi(data)
        return {
            "predicted_pm25": round(pm25_pred, 2)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ------------------------
# Gemini Insight Endpoint
# ------------------------
@app.post("/insights")
def gemini_insights(data: dict):
    try:
        pm25_pred = predict_aqi(data)
        pollutants = {k: data.get(k) for k in FEATURE_COLUMNS}

        try:
            explanation = generate_explanation(pm25_pred, pollutants)
        except Exception as llm_error:
            explanation = (
                "LLM insights are temporarily unavailable due to API quota limits. "
                "The predicted PM2.5 value can still be interpreted using standard AQI guidelines."
            )

        return {
            "predicted_pm25": round(pm25_pred, 2),
            "insight": explanation
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))



# ------------------------
# Model Evaluation Endpoint
# ------------------------
@app.get("/evaluation")
def model_evaluation():
    """
    Returns model performance metrics and feature importance.
    """
    eval_path = BASE_DIR / "models" / "evaluation.json"

    if not eval_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Evaluation file not found. Run training pipeline first."
        )

    with open(eval_path, "r") as f:
        evaluation_data = json.load(f)

    return evaluation_data
