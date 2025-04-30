from models.classification.random_forest import train_random_forest
from models.regression.linear_regression import train_linear_regression
from models.evaluation import evaluate_classification_model, evaluate_regression_model

# Train classification model
X_class = ...  # Features for classification
y_class = ...  # Labels for classification
model_class, accuracy, report = train_random_forest(X_class, y_class)

# Train regression model
X_reg = ...  # Features for regression
y_reg = ...  # Labels for regression
model_reg, mse, r2 = train_linear_regression(X_reg, y_reg)

# Evaluate classification model
accuracy, report = evaluate_classification_model(model_class, X_test_class, y_test_class)

# Evaluate regression model
mse, r2 = evaluate_regression_model(model_reg, X_test_reg, y_test_reg)
