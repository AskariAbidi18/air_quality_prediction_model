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

DATE_COLUMN = "Date"   # adjust if needed
TARGET_COLUMN = "AQI"  # or "AQI_Bucket"

FEATURE_COLUMNS = [
    "PM2.5",
    "PM10",
    "NO2",
    "SO2",
    "CO",
    "O3"
]

RANDOM_STATE = 42
TEST_SIZE = 0.2
