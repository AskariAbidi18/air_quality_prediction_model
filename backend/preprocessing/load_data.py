import pandas as pd 
from pathlib import Path

from utils.config import RAW_DATA_DIR, START_YEAR, END_YEAR, DATE_COLUMN

def load_and_merge_station_data():
    dataframes = []

    for csv_file in RAW_DATA_DIR.glob("*.csv"):

        if csv_file.name.lower() == "stations_info.csv":
            continue

        df = pd.read_csv(csv_file)

        df[DATE_COLUMN] = pd.to_datetime(df[DATE_COLUMN], errors='coerce')

        df = df.dropna(subset=[DATE_COLUMN])

        df = df[
            (df[DATE_COLUMN].dt.year >= START_YEAR) &
            (df[DATE_COLUMN].dt.year <= END_YEAR)
        ]

        station_code = csv_file.stem
        df["station_code"] = station_code 

        dataframes.append(df)

    if not dataframes:
        raise ValueError("No station data files found after filtering.")
    
    merged_df = pd.concat(dataframes, ignore_index=True)

    return merged_df
