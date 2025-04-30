from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "random_forest_model.pkl")


def train_random_forest(X, y, test_size=0.2, random_state=42):
    """Train and save a Random Forest Classifier."""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    model = RandomForestClassifier(n_estimators=100, random_state=random_state)
    model.fit(X_train, y_train)

    # Save the model
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    return model, accuracy, report

def load_random_forest_model():
    """Load the saved Random Forest model."""
    return joblib.load(MODEL_PATH)

def predict_zone(model, X_new):
    """Predict climate zones on new data."""
    return model.predict(X_new)
def load_random_forest_model():
    """Load a previously saved Random Forest model."""
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    else:
        raise FileNotFoundError(f"Model not found at {MODEL_PATH}. Please train and save it first.")