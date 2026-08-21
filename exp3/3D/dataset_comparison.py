"""
Experiment 3D: Comparison of Analysis Results Between UCI and Pima Diabetes Datasets

AIM:
To compare the statistical analysis results (Univariate, Bivariate, and Multiple Regression) of the
UCI Diabetes Dataset and the Pima Indians Diabetes Dataset.

NOTE:
The lab manual lists example placeholder scores for this comparison. Here the same metrics are
recomputed directly from the datasets so the comparison reflects the actual analysis results.
"""

import os
import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import r2_score, accuracy_score

numerical_columns = ["Glucose", "BloodPressure", "BMI"]

def summarise(df):
    """Univariate summary used for the central tendency / dispersion comparison."""
    rows = {}
    for col in numerical_columns:
        rows[col] = {
            "Mean": np.mean(df[col]),
            "Median": np.median(df[col]),
            "Variance": np.var(df[col], ddof=1),
            "Standard Deviation": np.std(df[col], ddof=1),
            "Skewness": skew(df[col]),
            "Kurtosis": kurtosis(df[col]),
        }
    return pd.DataFrame(rows).T

def multiple_regression_r2(df):
    X = df[["Glucose", "BloodPressure", "Age"]]
    y = df["BMI"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    return r2_score(y_test, model.predict(X_test))

def logistic_accuracy(df):
    X = df[["Glucose", "BloodPressure", "BMI", "Age"]]
    y = df["Outcome"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    return accuracy_score(y_test, model.predict(X_test))

def run_experiment_3d():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Load the Datasets
    uci_diabetes = pd.read_csv(os.path.join(base_dir, "uci_diabetes.csv"))
    pima_diabetes = pd.read_csv(os.path.join(base_dir, "pima_diabetes.csv"))

    # 1. Compare Univariate Analysis Results
    print("Comparison of Univariate Analysis Results:")
    print("\nUCI Diabetes Dataset Statistics:")
    print(summarise(uci_diabetes))
    print("\nPima Indians Diabetes Dataset Statistics:")
    print(summarise(pima_diabetes))

    # 2. Compare Regression Model Performance
    uci_r2 = multiple_regression_r2(uci_diabetes)
    pima_r2 = multiple_regression_r2(pima_diabetes)
    uci_accuracy = logistic_accuracy(uci_diabetes) * 100
    pima_accuracy = logistic_accuracy(pima_diabetes) * 100

    print("\n--- Model Performance Comparison ---")
    print(f"Multiple Regression R2 Scores: UCI - {uci_r2:.4f}, Pima - {pima_r2:.4f}")
    print(f"Logistic Regression Accuracy: UCI - {uci_accuracy:.1f}%, Pima - {pima_accuracy:.1f}%")

    # 3. Interpret the differences
    better = "UCI" if uci_r2 > pima_r2 else "Pima Indians"
    print(f"\nHigher multiple regression R2 score: {better} Diabetes dataset.")

if __name__ == "__main__":
    run_experiment_3d()
