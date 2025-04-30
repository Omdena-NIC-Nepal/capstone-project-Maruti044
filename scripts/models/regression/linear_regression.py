import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

def train_linear_regression(X, y, test_size=0.2, random_state=42, model_path='models/regression/linear_model.pkl'):
    """Train and save a Linear Regression model."""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Save the model
    joblib.dump(model, model_path)

    # Evaluation
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    return model, mse, r2

def load_linear_model(model_path='models/regression/linear_model.pkl'):
    """Load a trained Linear Regression model."""
    return joblib.load(model_path)

def predict_impact(X_new, model_path='models/regression/linear_model.pkl'):
    """Predict climate impact using the saved model."""
    model = load_linear_model(model_path)
    predictions = model.predict(X_new)
    return pd.Series(predictions, name="Predicted Impact")
