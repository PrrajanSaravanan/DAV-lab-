"""
Experiment 4B: Hypothesis Testing - Z-Test on UCI Diabetes Dataset

AIM:
To perform a Z-test on the UCI Diabetes dataset to determine whether the mean Glucose level
significantly differs from a given population mean (e.g., 100).

HYPOTHESES:
- H0 (Null): The mean Glucose level is equal to 100.
- H1 (Alternative): The mean Glucose level is significantly different from 100.
"""

import os
import pandas as pd
from statsmodels.stats.weightstats import ztest

def run_experiment_4b():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Load Dataset
    uci_diabetes = pd.read_csv(os.path.join(base_dir, "uci_diabetes.csv"))

    # Perform Z-Test for Glucose (Testing if mean Glucose differs from 100)
    z_stat, p_value = ztest(uci_diabetes["Glucose"], value=100)

    # Display Results
    print(f"Z-Statistic: {z_stat:.4f}")
    print(f"P-Value: {p_value:.4f}")

    # Interpretation
    alpha = 0.05  # 5% significance level
    if p_value < alpha:
        print("Reject the null hypothesis: The mean Glucose level is significantly different from 100.")
    else:
        print("Fail to reject the null hypothesis: No significant difference in mean Glucose level.")

if __name__ == "__main__":
    run_experiment_4b()
