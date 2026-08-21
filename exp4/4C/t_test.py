"""
Experiment 4C: Performing T-test on Diabetes Datasets

AIM:
To perform a T-test on the UCI Diabetes and Pima Indians Diabetes datasets to compare the means of
numerical variables and determine statistical significance.
"""

import os
import pandas as pd
from scipy.stats import ttest_ind

def run_experiment_4c():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Load the Datasets
    uci_diabetes = pd.read_csv(os.path.join(base_dir, "uci_diabetes.csv"))
    pima_diabetes = pd.read_csv(os.path.join(base_dir, "pima_diabetes.csv"))

    # Select Relevant Numerical Columns
    numerical_columns = ["Glucose", "BloodPressure", "BMI"]

    # Perform Independent T-test
    t_test_results = {}
    for col in numerical_columns:
        t_stat, p_value = ttest_ind(uci_diabetes[col], pima_diabetes[col], equal_var=False)
        t_test_results[col] = {"T-statistic": t_stat, "P-value": p_value}

    # Convert Results to DataFrame
    t_test_df = pd.DataFrame(t_test_results).T

    # Display Results
    print("\nT-test Results:\n", t_test_df)

    # Interpretation
    alpha = 0.05
    print("\nInterpretation (alpha = 0.05):")
    for col in numerical_columns:
        p = t_test_results[col]["P-value"]
        verdict = "significant difference" if p < alpha else "no significant difference"
        print(f"  {col}: p = {p:.4f} -> {verdict} between the two datasets.")

if __name__ == "__main__":
    run_experiment_4c()
