"""
Experiment 2D: Data Handling and Analysis - Descriptive Analytics Using the Iris Dataset
Aim: To explore descriptive analytics using the Iris dataset with Python's Pandas and Seaborn libraries.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
IRIS_PATH = os.path.join(BASE_DIR, "data", "raw", "iris.csv")
PLOTS_DIR = os.path.join(BASE_DIR, "data", "processed", "plots")

def run_experiment_2d():
    print("==================================================")
    print("EXPERIMENT 2D: DESCRIPTIVE ANALYTICS ON IRIS DATASET")
    print("==================================================")

    if not os.path.exists(IRIS_PATH):
        from src.utils.dataset_loader import load_all_datasets
        load_all_datasets()

    df = pd.read_csv(IRIS_PATH)
    os.makedirs(PLOTS_DIR, exist_ok=True)

    # 1. Display Basic Information & Summary Statistics
    print("\n--- Basic Information ---")
    print(df.info())

    print("\n--- Summary Statistics ---")
    print(df.describe())

    # 2. Univariate Analysis - Species Count
    print("\n--- Species Count ---")
    print(df['species'].value_counts())

    # 3. Visualize Data Distributions using Histograms
    print("\n[*] Generating Feature Distribution Histograms...")
    plt.figure(figsize=(8, 6))
    numeric_cols = [c for c in df.columns if c != 'species']
    df[numeric_cols].hist(figsize=(8, 6), edgecolor='black')
    plt.suptitle('Feature Distributions', fontsize=14)
    plt.tight_layout()
    hist_file = os.path.join(PLOTS_DIR, "iris_histograms.png")
    plt.savefig(hist_file)
    plt.close()
    print(f"[+] Saved histogram plot to {hist_file}")

    # 4. Boxplot for Sepal Length
    print("\n[*] Generating Boxplot for Sepal Length...")
    plt.figure(figsize=(7, 5))
    sns.boxplot(data=df, x='species', y='sepal length (cm)')
    plt.title('Sepal Length Comparison')
    plt.tight_layout()
    box_file = os.path.join(PLOTS_DIR, "iris_sepal_length_boxplot.png")
    plt.savefig(box_file)
    plt.close()
    print(f"[+] Saved boxplot to {box_file}")

    # 5. Pairplot to Analyze Feature Relationships
    print("\n[*] Generating Pairplot...")
    g = sns.pairplot(df, hue='species', palette='Set1')
    g.fig.suptitle('Iris Feature Relationships (Pairplot)', y=1.02)
    pair_file = os.path.join(PLOTS_DIR, "iris_pairplot.png")
    plt.savefig(pair_file)
    plt.close()
    print(f"[+] Saved pairplot to {pair_file}")

    print("\nRESULT: Descriptive analytics on the Iris dataset using Pandas and Seaborn completed successfully, providing insights into feature distributions and species differentiation.")

if __name__ == "__main__":
    run_experiment_2d()
