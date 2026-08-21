"""
Experiment 5B: Building and Validating Logistic Models

AIM:
To build and validate Logistic Regression Models for predicting diabetes presence using the UCI and
Pima Indians Diabetes datasets.

MODEL VALIDATION METRICS:
- Accuracy Score: measures correct classifications.
- Precision & Recall: measures class-wise performance.
- F1 Score: balances precision and recall.
- Confusion Matrix: evaluates prediction errors.
"""

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, confusion_matrix)

# Select Features and Target Variable
features = ["Glucose", "BloodPressure", "BMI"]
target = "Outcome"  # Target variable indicating diabetes presence

def build_and_validate(df):
    X = df[features]
    y = df[target]

    # Split Data into Training and Testing Sets (80%-20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the Logistic Regression Model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Make Predictions
    y_pred = model.predict(X_test)

    return y_test, y_pred

def report(dataset_name, y_test, y_pred):
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, zero_division=0)
    recall = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)

    print(f"{dataset_name} - Logistic Regression Results:")
    print(f"Accuracy: {accuracy:.4f}, Precision: {precision:.4f}, "
          f"Recall: {recall:.4f}, F1 Score: {f1:.4f}\n")

def run_experiment_5b():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Load the Datasets
    uci_diabetes = pd.read_csv(os.path.join(base_dir, "uci_diabetes.csv"))
    pima_diabetes = pd.read_csv(os.path.join(base_dir, "pima_diabetes.csv"))

    y_test_uci, y_pred_uci = build_and_validate(uci_diabetes)
    y_test_pima, y_pred_pima = build_and_validate(pima_diabetes)

    report("UCI Diabetes Dataset", y_test_uci, y_pred_uci)
    report("Pima Indians Diabetes Dataset", y_test_pima, y_pred_pima)

    # Plot Confusion Matrices
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    sns.heatmap(confusion_matrix(y_test_uci, y_pred_uci), annot=True, fmt='d',
                cmap='Blues', ax=axes[0])
    axes[0].set_title("UCI Diabetes - Confusion Matrix")
    axes[0].set_xlabel("Predicted")
    axes[0].set_ylabel("Actual")

    sns.heatmap(confusion_matrix(y_test_pima, y_pred_pima), annot=True, fmt='d',
                cmap='Blues', ax=axes[1])
    axes[1].set_title("Pima Indians Diabetes - Confusion Matrix")
    axes[1].set_xlabel("Predicted")
    axes[1].set_ylabel("Actual")

    plt.tight_layout()
    plt.savefig(os.path.join(base_dir, "confusion_matrices.png"), bbox_inches='tight')
    plt.close()
    print("Saved confusion matrices to 'confusion_matrices.png'")

if __name__ == "__main__":
    run_experiment_5b()
