"""
Experiment 5A: Building and Validating Linear Models

AIM:
To build and validate Linear Regression Models using the UCI and Pima Indians Diabetes datasets.

MODEL VALIDATION METRICS:
- R2 Score (Coefficient of Determination): how well the model explains variability.
- Mean Squared Error (MSE): average squared errors.
- Mean Absolute Error (MAE): average absolute errors.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# Select Features and Target Variable
features = ["Glucose", "BloodPressure", "BMI"]
target = "Age"

def build_and_validate(df, dataset_name, base_dir, save_filename):
    X = df[features]
    y = df[target]

    # Split Data into Training and Testing Sets (80%-20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the Linear Regression Model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make Predictions
    y_pred = model.predict(X_test)

    # Evaluate Model Performance
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    print(f"{dataset_name} - Linear Regression Results:")
    print(f"R2 Score: {r2:.4f}, MSE: {mse:.4f}, MAE: {mae:.4f}")

    # Visualize predictions vs. actual values
    plt.figure(figsize=(6, 5))
    plt.scatter(y_test, y_pred, color='blue', alpha=0.7)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', linewidth=2)
    plt.xlabel(f"Actual {target}")
    plt.ylabel(f"Predicted {target}")
    plt.title(f"{dataset_name}: Predicted vs. Actual")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.savefig(os.path.join(base_dir, save_filename), bbox_inches='tight')
    plt.close()
    print(f"Saved plot to '{save_filename}'\n")

def run_experiment_5a():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Load the Datasets
    uci_diabetes = pd.read_csv(os.path.join(base_dir, "uci_diabetes.csv"))
    pima_diabetes = pd.read_csv(os.path.join(base_dir, "pima_diabetes.csv"))

    build_and_validate(uci_diabetes, "UCI Diabetes Dataset", base_dir, "uci_predicted_vs_actual.png")
    build_and_validate(pima_diabetes, "Pima Indians Diabetes Dataset", base_dir, "pima_predicted_vs_actual.png")

if __name__ == "__main__":
    run_experiment_5a()
