import pandas as pd

from utils.config import FEATURE_COLUMNS, TARGET_COLUMN, DATE_COLUMN

def prepare_features_and_target(df: pd.DataFrame):
    df = df.copy()

    if DATE_COLUMN in df.columns:
        df["month"] = pd.to_datetime(df[DATE_COLUMN]).dt.month

    feature_cols = FEATURE_COLUMNS.copy()
    if "month" in df.columns:
        feature_cols.append("month")

    X = df[feature_cols]
    y = df[TARGET_COLUMN]

    return X, y 
