# backend/utils/config.py

from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

MODEL_DIR = BASE_DIR / "models"
MODEL_PATH = MODEL_DIR / "model.pkl"

# Project-specific settings
CITY_NAME = "Lucknow"

START_YEAR = 2019
END_YEAR = 2023

DATE_COLUMN = "From Date"   # adjust if needed
TARGET_COLUMN = "PM2.5 (ug/m3)"  # or "AQI_Bucket"

FEATURE_COLUMNS = [
    "PM10 (ug/m3)",
    "NO2 (ug/m3)",
    "SO2 (ug/m3)",
    "CO (mg/m3)",
    "Ozone (ug/m3)"
]

RANDOM_STATE = 42
TEST_SIZE = 0.2

POLLUTANT_THRESHOLDS = {
    "PM10 (ug/m3)": 100,
    "NO2 (ug/m3)": 80,
    "SO2 (ug/m3)": 80,
    "CO (mg/m3)": 2,
    "Ozone (ug/m3)": 100
}

