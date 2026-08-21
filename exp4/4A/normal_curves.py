"""
Experiment 4A: Data Visualization - Normal Curves on UCI Diabetes Dataset

AIM:
To visualize the distribution of key numerical attributes in the UCI Diabetes dataset using normal
curves.
"""

import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm

def run_experiment_4a():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Load Dataset
    uci_diabetes = pd.read_csv(os.path.join(base_dir, "uci_diabetes.csv"))

    # Plot Normal Curves for Glucose and BMI
    plt.figure(figsize=(12, 5))

    # Normal Curve for Glucose
    plt.subplot(1, 2, 1)
    sns.histplot(uci_diabetes["Glucose"], kde=True, stat="density", linewidth=0)
    x = np.linspace(uci_diabetes["Glucose"].min(), uci_diabetes["Glucose"].max(), 100)
    plt.plot(x, norm.pdf(x, uci_diabetes["Glucose"].mean(), uci_diabetes["Glucose"].std()), 'r')
    plt.title("Normal Curve - Glucose")

    # Normal Curve for BMI
    plt.subplot(1, 2, 2)
    sns.histplot(uci_diabetes["BMI"], kde=True, stat="density", linewidth=0)
    x = np.linspace(uci_diabetes["BMI"].min(), uci_diabetes["BMI"].max(), 100)
    plt.plot(x, norm.pdf(x, uci_diabetes["BMI"].mean(), uci_diabetes["BMI"].std()), 'r')
    plt.title("Normal Curve - BMI")

    out_path = os.path.join(base_dir, "normal_curves.png")
    plt.savefig(out_path, bbox_inches='tight')
    plt.close()
    print("Saved normal curves to 'normal_curves.png'")

if __name__ == "__main__":
    run_experiment_4a()
