import joblib 
import pandas as pd

from utils.config import MODEL_PATH, FEATURE_COLUMNS

model = joblib.load(MODEL_PATH)

def predict_aqi(input_data: dict) -> float:
    df = pd.DataFrame([input_data])
    df = df[[col for col in FEATURE_COLUMNS if col in df.columns]]

    prediction = model.predict(df)[0]

    return float(prediction)
