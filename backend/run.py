import json

from preprocessing.load_data import load_and_merge_station_data
from preprocessing.clean_data import clean_air_quality_data
from preprocessing.feature_engineering import prepare_features_and_target

from modeling.train_model import train_random_forest
from modeling.evaluate_model import evaluate_regression_model

from utils.config import PROCESSED_DATA_DIR, BASE_DIR

def run_pipeline():
    print("Loading annd merging station data...")
    df= load_and_merge_station_data()

    print("Cleaning air quality data...")
    df_clean = clean_air_quality_data(df)

    PROCESSED_DATA_DIR.mkdir(exist_ok=True)
    processed_path = PROCESSED_DATA_DIR / "lucknow_2019_2023.csv"
    df_clean.to_csv(processed_path, index=False)
    print(f"Processed dataset saved at {processed_path}")

    print("Feature Engineering...")
    X, y = prepare_features_and_target(df_clean)

    print("Training model...")
    model, X_test, y_test = train_random_forest(X, y)

    print("Evaluating model...")
    eval_results = evaluate_regression_model(
        model, X_test, y_test, plot=True
    )

    eval_path = BASE_DIR / "models" / "evaluation.json"
    with open(eval_path, "w") as f:
        json.dump(eval_results, f, indent=4)

    print(f"Evaluation results saved at {eval_path}")
    print("Pipeline completed successfully.")

if __name__ == "__main__":
    run_pipeline()

