import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score

def evaluate_regression_model(model, X_test, y_test, plot = False):
    y_pred = model.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    feature_importances = dict(
        zip(X_test.columns, model.feature_importances_)
    )

    if plot:
        _plot_feature_importance(feature_importances)

    return {
        "rmse": round(float(rmse), 2),
        "r2_score": round(float(r2), 3),
        "feature_importance": feature_importances
    }

def _plot_feature_importance(feature_importances):
    features = list(feature_importances.keys())
    values = list(feature_importances.values())

    indices = np.argsort(values)

    plt.figure(figsize=(8, 5))
    plt.barh(
        [features[i] for i in indices],
        [values[i] for i in indices]
    )
    plt.xlabel("Feature Importance")
    plt.title("Pollutant Contribution to AQI")
    plt.tight_layout()
    plt.show()
