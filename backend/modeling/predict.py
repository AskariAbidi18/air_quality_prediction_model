import pandas as pd
import joblib

from backend.utils.config import MODEL_PATH, FEATURE_COLUMNS

# Load trained model once
model = joblib.load(MODEL_PATH)

print("Model expects features:", model.feature_names_in_)


def predict_aqi(input_data: dict) -> float:
    # Build input row with correct feature order
    row = {}
    for feature in FEATURE_COLUMNS:
        if feature not in input_data:
            raise ValueError(f"Missing required feature: {feature}")
        row[feature] = input_data[feature]

    X = pd.DataFrame([row], columns=FEATURE_COLUMNS)

    prediction = model.predict(X)[0]
    return float(prediction)
