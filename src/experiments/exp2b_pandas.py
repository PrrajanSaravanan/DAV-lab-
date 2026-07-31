"""
Experiment 2B: Data Handling and Analysis - Working with Pandas DataFrames
Aim: To explore and perform various DataFrame operations using Pandas, including loading datasets, data inspection,
handling missing values, transformations, filtering, grouping, sorting, and saving results.
"""

import os
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "Google_data.csv")
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "filtered_data.csv")

def run_experiment_2b():
    print("==================================================")
    print("EXPERIMENT 2B: WORKING WITH PANDAS DATAFRAMES")
    print("==================================================")

    # 1. Load dataset into DataFrame
    if not os.path.exists(RAW_DATA_PATH):
        from src.utils.dataset_loader import load_all_datasets
        load_all_datasets()

    df = pd.read_csv(RAW_DATA_PATH)
    print("\n[+] Dataset Loaded Successfully!")

    # 2. Display first and last few rows
    print("\n--- First 5 Rows ---")
    print(df.head())
    print("\n--- Last 5 Rows ---")
    print(df.tail())

    # 3. Check data types and general info
    print("\n--- DataFrame Information ---")
    df.info()

    # 4. Summary statistics
    print("\n--- Summary Statistics ---")
    print(df.describe())

    # 5. Handle missing values
    print("\n--- Handling Missing Values ---")
    df['Rating'] = df['Rating'].fillna(df['Rating'].mean())
    print("Filled missing values in 'Rating' column with mean.")

    # 6. Create a new column
    # Convert 'Reviews' to numeric for column creation & filtering
    df['Reviews_num'] = pd.to_numeric(df['Reviews'], errors='coerce').fillna(0)
    df['Reviews_double'] = df['Reviews_num'] * 2
    print("\n[+] Created new column 'Reviews_double'")

    # 7. Create a Series and perform operations
    series_rating = df['Rating']
    print("\n--- Series Addition (Rating + 0.5) ---")
    print((series_rating + 0.5).head())

    # 8. Filter rows based on conditions
    filtered_df = df[(df['Rating'] >= 4.5) & (df['Reviews_num'] > 100)]
    print(f"\n--- Filtered Rows (Rating >= 4.5 & Reviews > 100): {len(filtered_df)} rows ---")
    print(filtered_df[['App', 'Category', 'Rating', 'Reviews_num']])

    # 9. Grouping and Aggregation
    print("\n--- Grouping by Category and Computing Mean Rating ---")
    grouped = df.groupby('Category')['Rating'].mean()
    print(grouped)

    # 10. Sorting
    print("\n--- Sorted DataFrame by Rating (Descending) ---")
    df_sorted = df.sort_values(by='Rating', ascending=False)
    print(df_sorted[['App', 'Category', 'Rating']].head())

    # 11. Boolean Masking
    median_rating = df['Rating'].median()
    masked_df = df[df['Rating'] > median_rating]
    print(f"\n--- Masked DataFrame (Rating > median {median_rating}) ---")
    print(masked_df[['App', 'Rating']].head())

    # 12. Remove duplicates and drop missing values
    df_clean = df.drop_duplicates().dropna()
    print(f"\n[+] Data Cleaned: {len(df_clean)} rows remaining")

    # 13. Create subset and save to CSV
    subset_df = df_clean[['App', 'Category', 'Rating', 'Reviews_num']]
    os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
    subset_df.to_csv(PROCESSED_DATA_PATH, index=False)
    print(f"[+] Saved subset DataFrame to {PROCESSED_DATA_PATH}")

    # 14. Compute summary statistics
    print("\n--- Summary Statistics on Reviews_num ---")
    print("Total Sum:", df['Reviews_num'].sum())
    print("Mean:", df['Reviews_num'].mean())
    print("Standard Deviation:", df['Reviews_num'].std())

    print("\nRESULT: Pandas DataFrame operations including data inspection, cleaning, transformation, filtering, grouping, sorting, and exporting completed successfully.")

if __name__ == "__main__":
    run_experiment_2b()
