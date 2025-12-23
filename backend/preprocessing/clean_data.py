import pandas as pd

from utils.config import FEATURE_COLUMNS, TARGET_COLUMN 

def clean_air_quality_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df = df.dropna(subset=TARGET_COLUMN)

    for feature in FEATURE_COLUMNS:
        if feature in df.columns:
            median_value = df[feature].median()
            df[feature] = df[feature].fillna(median_value)
        else:
            df = df.drop(columns=[feature], errors="ignore")

    df = df.drop_duplicates()

    return df 
