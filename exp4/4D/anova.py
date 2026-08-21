"""
Experiment 4D: Perform ANOVA on Diabetes Datasets

AIM:
To perform ANOVA (Analysis of Variance) on the UCI Diabetes and Pima Indians Diabetes datasets to
analyze differences between multiple group means.

DECISION RULE:
- p < 0.05: Significant difference exists between groups.
- p >= 0.05: No significant difference.
"""

import os
import pandas as pd
from scipy.stats import f_oneway

def run_experiment_4d():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Load the Datasets
    uci_diabetes = pd.read_csv(os.path.join(base_dir, "uci_diabetes.csv"))
    pima_diabetes = pd.read_csv(os.path.join(base_dir, "pima_diabetes.csv"))

    # Select Relevant Numerical Columns
    numerical_columns = ["Glucose", "BloodPressure", "BMI"]

    # Perform One-Way ANOVA
    anova_results = {}
    for col in numerical_columns:
        f_stat, p_value = f_oneway(uci_diabetes[col], pima_diabetes[col])
        anova_results[col] = {"F-statistic": f_stat, "P-value": p_value}

    # Convert Results to DataFrame
    anova_df = pd.DataFrame(anova_results).T

    # Display Results
    print("\nANOVA Results:\n", anova_df)

    # Interpretation
    alpha = 0.05
    print("\nInterpretation (alpha = 0.05):")
    for col in numerical_columns:
        p = anova_results[col]["P-value"]
        verdict = "significant difference" if p < alpha else "no significant difference"
        print(f"  {col}: p = {p:.4f} -> {verdict} between the group means.")

if __name__ == "__main__":
    run_experiment_4d()
