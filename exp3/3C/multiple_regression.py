"""
Experiment 3C: Multiple Regression Analysis

AIM:
To perform multiple regression analysis on the UCI Diabetes and Pima Indians Diabetes datasets to
predict BMI based on multiple independent variables.
"""

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Select Relevant Features and Target Variable
features = ["Glucose", "BloodPressure", "Age"]
target = "BMI"

def multiple_regression_analysis(df, dataset_name):
    # Extract Features and Target Variable
    X = df[features]
    y = df[target]

    # Split Data into Training and Testing Sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and Train the Model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict and Evaluate the Model
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)

    print(f"\n{dataset_name} - Multiple Regression R2 Score: {r2:.4f}")

def run_experiment_3c():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Load the Datasets
    uci_diabetes = pd.read_csv(os.path.join(base_dir, "uci_diabetes.csv"))
    pima_diabetes = pd.read_csv(os.path.join(base_dir, "pima_diabetes.csv"))

    # Perform Multiple Regression on Both Datasets
    multiple_regression_analysis(uci_diabetes, "UCI Diabetes Dataset")
    multiple_regression_analysis(pima_diabetes, "Pima Indians Diabetes Dataset")

if __name__ == "__main__":
    run_experiment_3c()
