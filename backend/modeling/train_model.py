import joblib 
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

from utils.config import MODEL_PATH, TEST_SIZE, RANDOM_STATE

def train_random_forest(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE
    )

    model = RandomForestRegressor(
        random_state = RANDOM_STATE, 
        n_estimators = 200, 
        n_jobs = -1
    )

    model.fit(X_train, y_train)

    MODEL_PATH.parent.mkdir(exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    return model, X_test, y_test
