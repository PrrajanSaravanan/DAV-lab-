"""
Experiment 3A: Statistical Analysis Using Diabetes Datasets - Univariate Analysis
Aim: To analyze the Diabetes dataset from UCI and the Pima Indians Diabetes dataset using univariate statistical methods,
including Frequency, Mean, Median, Mode, Variance, Standard Deviation, Skewness, and Kurtosis.
"""

import os
import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UCI_DIABETES_PATH = os.path.join(BASE_DIR, "data", "raw", "uci_diabetes.csv")
PIMA_DIABETES_PATH = os.path.join(BASE_DIR, "data", "raw", "pima_diabetes.csv")

def univariate_analysis(df, columns):
    """Compute univariate statistical measures for selected numerical columns."""
    stats = {}
    for col in columns:
        stats[col] = {
            "Mean": np.mean(df[col]),
            "Median": np.median(df[col]),
            "Mode": df[col].mode()[0],
            "Variance": np.var(df[col], ddof=1),
            "Standard Deviation": np.std(df[col], ddof=1),
            "Skewness": skew(df[col]),
            "Kurtosis": kurtosis(df[col])
        }
    return pd.DataFrame(stats).T

def run_experiment_3a():
    print("==================================================")
    print("EXPERIMENT 3A: UNIVARIATE STATISTICAL ANALYSIS ON DIABETES DATASETS")
    print("==================================================")

    if not (os.path.exists(UCI_DIABETES_PATH) and os.path.exists(PIMA_DIABETES_PATH)):
        from src.utils.dataset_loader import load_all_datasets
        load_all_datasets()

    uci_diabetes = pd.read_csv(UCI_DIABETES_PATH)
    pima_diabetes = pd.read_csv(PIMA_DIABETES_PATH)

    print("\n[+] UCI Diabetes Dataset Sample (Head 5):")
    print(uci_diabetes.head())

    print("\n[+] Pima Indians Diabetes Dataset Sample (Head 5):")
    print(pima_diabetes.head())

    numerical_columns = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]

    # Perform Univariate Analysis
    uci_stats = univariate_analysis(uci_diabetes, numerical_columns)
    pima_stats = univariate_analysis(pima_diabetes, numerical_columns)

    print("\n==================================================")
    print("UCI Diabetes Dataset Statistics:")
    print("==================================================")
    print(uci_stats.to_string())

    print("\n==================================================")
    print("Pima Indians Diabetes Dataset Statistics:")
    print("==================================================")
    print(pima_stats.to_string())

    print("\nRESULT: The univariate analysis of the UCI Diabetes and Pima Indians Diabetes datasets reveals differences in central tendency, dispersion, and distribution. Variations in skewness and kurtosis indicate differences in data patterns between the datasets.")

if __name__ == "__main__":
    run_experiment_3a()
