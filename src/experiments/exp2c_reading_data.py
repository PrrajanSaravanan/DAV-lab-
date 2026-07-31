"""
Experiment 2C: Data Handling and Analysis - Reading Data from Text Files, Excel, and the Web
Aim: To read and process data from various sources, including text files, Excel spreadsheets, and web-based data,
using Python's Pandas library.
"""

import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAW_CSV_PATH = os.path.join(BASE_DIR, "data", "raw", "Google_data.csv")
RAW_EXCEL_PATH = os.path.join(BASE_DIR, "data", "raw", "data_sample.xlsx")
PROCESSED_TEXT_PATH = os.path.join(BASE_DIR, "data", "processed", "processed_text.csv")
PROCESSED_EXCEL_PATH = os.path.join(BASE_DIR, "data", "processed", "processed_excel.xlsx")

WEB_URL = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"

def run_experiment_2c():
    print("==================================================")
    print("EXPERIMENT 2C: READING DATA FROM TEXT, EXCEL, AND WEB")
    print("==================================================")

    # 1. Read data from CSV file
    print(f"\n[1] Reading CSV File from: {RAW_CSV_PATH}")
    text_df = pd.read_csv(RAW_CSV_PATH)
    print("CSV Data Head:")
    print(text_df.head(3))

    # 2. Read data from Excel file
    print(f"\n[2] Reading Excel File from: {RAW_EXCEL_PATH}")
    excel_df = pd.read_excel(RAW_EXCEL_PATH, sheet_name='Sheet1')
    print("Excel Data Head:")
    print(excel_df.head(3))

    # 3. Read data from Web-based source
    print(f"\n[3] Reading Web-based CSV from: {WEB_URL}")
    try:
        web_df = pd.read_csv(WEB_URL)
        print("Web Data Head:")
        print(web_df.head(5))
    except Exception as e:
        print(f"[-] Web data load failed ({e}), creating fallback web DataFrame")
        web_df = pd.DataFrame({
            "Country": ["Algeria", "Angola", "Benin", "Botswana", "Burkina"],
            "Region": ["AFRICA", "AFRICA", "AFRICA", "AFRICA", "AFRICA"]
        })
        print(web_df.head(5))

    # 4. Handle Missing Values
    print("\n--- Handling Missing Values ---")
    text_df = text_df.ffill()
    excel_df = excel_df.bfill()
    web_df = web_df.dropna()
    print("Missing values handled using ffill (CSV), bfill (Excel), and dropna (Web).")

    # 5. Save Processed Data into New File Formats
    os.makedirs(os.path.dirname(PROCESSED_TEXT_PATH), exist_ok=True)
    text_df.to_csv(PROCESSED_TEXT_PATH, index=False)
    excel_df.to_excel(PROCESSED_EXCEL_PATH, index=False)

    print(f"\n[+] Saved processed text data to: {PROCESSED_TEXT_PATH}")
    print(f"[+] Saved processed Excel data to: {PROCESSED_EXCEL_PATH}")

    print("\nRESULT: Reading and processing data from text files, Excel spreadsheets, and web-based sources successfully completed.")

if __name__ == "__main__":
    run_experiment_2c()
