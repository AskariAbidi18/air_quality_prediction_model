from google import genai
import os
from utils.config import POLLUTANT_THRESHOLDS

# Initialize Gemini client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

MODEL_NAME = "models/gemini-pro-latest"


def _get_high_pollutants(pollutants: dict):
    high = []
    for pollutant, value in pollutants.items():
        threshold = POLLUTANT_THRESHOLDS.get(pollutant)
        if threshold is not None and value is not None and value > threshold:
            high.append(pollutant)
    return high


def generate_explanation(predicted_pm25: float, pollutants: dict) -> str:
    high_pollutants = _get_high_pollutants(pollutants)
    high_text = ", ".join(high_pollutants) if high_pollutants else "None"

    prompt = f"""
    You are an air quality and environmental health expert.

    City: Lucknow
    Predicted PM2.5 concentration: {predicted_pm25:.2f} µg/m³

    Observed pollutant concentrations:
    {pollutants}

    Pollutants exceeding safe guideline levels:
    {high_text}

    Reference: Indian AQI (PM2.5, 24-hour average)
    0–30    → Good
    31–60   → Satisfactory
    61–90   → Moderate
    91–120  → Poor
    121–250 → Very Poor
    >250    → Severe

    Tasks:
    1. Explain what this PM2.5 concentration indicates about overall air quality.
    2. Describe the likely short-term and long-term health effects at this level.
    3. Briefly explain the role of each pollutant that exceeds safe levels.
    4. Based on the PM2.5 value and the reference above, mention the approximate AQI category and an approximate AQI range this level corresponds to.
    - Do NOT calculate or claim an exact AQI value.
    - Clearly state that this is an approximate interpretation for understanding only.

    Keep the explanation concise, factual, and easy to understand for a general audience.
    """

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text.strip()
