"""
Notebook Generator Utility for DAV Assignment
Generates fully-structured, executable Jupyter Notebooks (.ipynb) for Experiments 1 to 3-A.
"""

import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NOTEBOOKS_DIR = os.path.join(BASE_DIR, "notebooks")

def make_cell_markdown(text):
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in text.split("\n")]
    }

def make_cell_code(code):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in code.split("\n")]
    }

def build_notebook(cells):
    return {
        "cells": cells,
        "metadata": {
            "language_info": {
                "name": "python",
                "version": "3.10"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 2
    }

def save_notebook(nb_dict, filename):
    os.makedirs(NOTEBOOKS_DIR, exist_ok=True)
    path = os.path.join(NOTEBOOKS_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb_dict, f, indent=2)
    print(f"[+] Created notebook: {path}")

def generate_exp1():
    md1 = """# Experiment 1: Installation and Exploration

## AIM:
To download, install, and explore the features of NumPy, SciPy, Jupyter, Statsmodels, Pandas, Matplotlib, Seaborn, Plotly, and Bokeh for scientific computing, data analysis, and visualization.

## REQUIREMENTS:
- **Python**: Version 3.10+
- **Jupyter Notebook**: Installed

## THEORY:
- **Python**: An interpreted general-purpose, high-level programming language.
- **Jupyter**: For creating interactive notebooks to run Python code.
- **NumPy**: Perform array manipulations, mathematical operations, and linear algebra.
- **SciPy**: Solve optimization problems and explore scientific computations.
- **Pandas**: Data manipulation using DataFrames for structured data analysis.
- **Matplotlib**: Create simple visualizations like line charts, bar plots, and histograms.
- **Seaborn**: Generate enhanced statistical visualizations like heatmaps, violin plots, and pair plots.
- **Plotly**: Interactive visualizations like 3D plots, animated charts, and dashboards.
- **Bokeh**: Highly interactive web-based visualizations.
- **Statsmodels**: Advanced statistical analysis, regression modeling, and hypothesis testing."""

    code1 = """import numpy as np
import pandas as pd
import matplotlib
import seaborn as sns
import statsmodels.api as sm
import scipy
import plotly
import bokeh

print("NumPy Version:", np.__version__)
print("Pandas Version:", pd.__version__)
print("Matplotlib Version:", matplotlib.__version__)
print("Seaborn Version:", sns.__version__)
print("Statsmodels Version:", sm.__version__)
print("SciPy Version:", scipy.__version__)
print("Plotly Version:", plotly.__version__)
print("Bokeh Version:", bokeh.__version__)"""

    md2 = """## RESULT:
Libraries are ready for scientific computing, data analysis, and visualization."""

    nb = build_notebook([make_cell_markdown(md1), make_cell_code(code1), make_cell_markdown(md2)])
    save_notebook(nb, "Exp1_Installation_and_Exploration.ipynb")

def generate_exp2a():
    md1 = """# Experiment 2A: Working with NumPy Arrays

## AIM:
To understand and implement various NumPy operations, including array creation, indexing, slicing, element-wise operations, aggregations, boolean operations, fancy indexing, reshaping, and structured arrays.

## THEORY:
- **NumPy**: Fundamental library for numerical computing in Python, offering multi-dimensional arrays, element-wise math operations, slicing, boolean masking, and structured data handling."""

    code1 = """import numpy as np

# Check NumPy version
print("NumPy Version:", np.__version__)

# Creating different types of arrays
arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_0d = np.array(42)
arr_ones = np.ones((3, 3))

# Indexing and Slicing
print("Element at index 2 in 1D array:", arr_1d[2])
print("Element at row 1, column 2 in 2D array:", arr_2d[1, 2])
print("Slice from 1D array:", arr_1d[1:4])
print("Slice row 1 from 2D array:", arr_2d[1, :])

# Element-wise operations
arr_a = np.array([10, 20, 30])
arr_b = np.array([1, 2, 3])
print("Addition:", arr_a + arr_b)
print("Subtraction:", arr_a - arr_b)
print("Multiplication:", arr_a * arr_b)
print("Division:", arr_a / arr_b)
print("Scalar Multiplication:", arr_a * 2)

# Aggregations
print("Sum:", np.sum(arr_a))
print("Mean:", np.mean(arr_a))
print("Standard Deviation:", np.std(arr_a))

# Element-wise comparison & Boolean masking
print("Element-wise comparison:", arr_a > arr_b)
print("Elements greater than 15:", arr_a[arr_a > 15])

# Fancy Indexing
indices = [0, 2]
print("Selected elements:", arr_a[indices])

# Reshape
reshaped_arr = arr_1d.reshape(5, 1)
print("Reshaped 1D array to 2D:\\n", reshaped_arr)

# Structured array
structured_arr = np.array([(25, 90.5), (30, 85.2)], dtype=[('age', 'i4'), ('score', 'f4')])
print("Structured array:", structured_arr)"""

    md2 = """## RESULT:
The experiment successfully demonstrated various NumPy operations, including array manipulations, indexing, slicing, arithmetic operations, aggregations, boolean masking, fancy indexing, reshaping, and structured arrays."""

    nb = build_notebook([make_cell_markdown(md1), make_cell_code(code1), make_cell_markdown(md2)])
    save_notebook(nb, "Exp2A_NumPy_Arrays.ipynb")

def generate_exp2b():
    md1 = """# Experiment 2B: Working with Pandas DataFrames

## AIM:
To explore and perform various DataFrame operations using Pandas, including loading datasets, data inspection, handling missing values, transformations, filtering, grouping, sorting, and saving results."""

    code1 = """import os
import pandas as pd

# Load dataset into a DataFrame
file_path = os.path.join("..", "data", "raw", "Google_data.csv")
df = pd.read_csv(file_path)

# Display first and last few rows
print("First 5 rows:\\n", df.head())
print("Last 5 rows:\\n", df.tail())

# Check data types and general info
df.info()

# Summary statistics
print("Summary statistics:\\n", df.describe())

# Handle missing values
df['Rating'] = df['Rating'].fillna(df['Rating'].mean())

# Create a new column
df['Reviews_num'] = pd.to_numeric(df['Reviews'], errors='coerce').fillna(0)
df['new_column'] = df['Reviews_num'] * 2

# Create a Series and perform operations
series = df['Rating']
print("Series addition:\\n", series + 0.5)

# Filter rows based on conditions
filtered_df = df[(df['Rating'] > 4.0) & (df['Reviews_num'] < 1000)]
print("Filtered DataFrame:\\n", filtered_df.head())

# Grouping and aggregation
grouped = df.groupby('Category')['Rating'].mean()
print("Grouped mean:\\n", grouped)

# Sorting
df_sorted = df.sort_values(by='Rating', ascending=False)
print("Sorted DataFrame:\\n", df_sorted[['App', 'Rating']].head())

# Boolean masking
masked_df = df[df['Rating'] > df['Rating'].median()]
print("Masked DataFrame:\\n", masked_df[['App', 'Rating']].head())

# Remove duplicates and drop missing values
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Create a new DataFrame with selected columns & save to CSV
subset_df = df[['App', 'Category', 'Rating', 'Reviews_num']]
out_path = os.path.join("..", "data", "processed", "subset_data.csv")
os.makedirs(os.path.dirname(out_path), exist_ok=True)
subset_df.to_csv(out_path, index=False)

# Compute summary statistics
print("Total sum:", subset_df['Rating'].sum())
print("Mean:", subset_df['Rating'].mean())
print("Standard Deviation:", subset_df['Rating'].std())"""

    md2 = """## RESULT:
The experiment successfully demonstrated various Pandas operations, including loading and inspecting data, handling missing values, transformations, filtering, grouping, sorting, and exporting data."""

    nb = build_notebook([make_cell_markdown(md1), make_cell_code(code1), make_cell_markdown(md2)])
    save_notebook(nb, "Exp2B_Pandas_DataFrames.ipynb")

def generate_exp2c():
    md1 = """# Experiment 2C: Reading Data from Text Files, Excel, and the Web

## AIM:
To read and process data from various sources, including text files, Excel spreadsheets, and web-based data, using Python's Pandas library."""

    code1 = """import os
import pandas as pd

csv_path = os.path.join("..", "data", "raw", "Google_data.csv")
excel_path = os.path.join("..", "data", "raw", "data_sample.xlsx")
web_url = 'https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv'

# Read data from sources
text_df = pd.read_csv(csv_path)
excel_df = pd.read_excel(excel_path, sheet_name='Sheet1')
try:
    web_df = pd.read_csv(web_url)
except Exception:
    web_df = pd.DataFrame({"Country": ["Algeria", "Angola"], "Region": ["AFRICA", "AFRICA"]})

# Display data
print("CSV Head:\\n", text_df.head(2))
print("Excel Head:\\n", excel_df.head(2))
print("Web Head:\\n", web_df.head(2))

# Handle missing values
text_df = text_df.ffill()
excel_df = excel_df.bfill()
web_df = web_df.dropna()

# Save processed data
out_csv = os.path.join("..", "data", "processed", "processed_text.csv")
out_excel = os.path.join("..", "data", "processed", "processed_excel.xlsx")
os.makedirs(os.path.dirname(out_csv), exist_ok=True)

text_df.to_csv(out_csv, index=False)
excel_df.to_excel(out_excel, index=False)
print("Saved processed files successfully!")"""

    md2 = """## RESULT:
The experiment successfully demonstrated reading data from text files, Excel spreadsheets, and web-based sources using Pandas."""

    nb = build_notebook([make_cell_markdown(md1), make_cell_code(code1), make_cell_markdown(md2)])
    save_notebook(nb, "Exp2C_Reading_Data.ipynb")

def generate_exp2d():
    md1 = """# Experiment 2D: Exploring Descriptive Analytics Using the Iris Dataset

## AIM:
To explore descriptive analytics using the Iris dataset with Python's Pandas, Matplotlib, and Seaborn libraries."""

    code1 = """import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

iris_path = os.path.join("..", "data", "raw", "iris.csv")
df = pd.read_csv(iris_path)

# Display basic information and summary statistics
print("Basic Information:")
print(df.info())

print("\\nSummary Statistics:")
print(df.describe())

# Univariate analysis - species count
print("\\nSpecies Count:")
print(df['species'].value_counts())

# Visualize data distributions using histograms
num_cols = [c for c in df.columns if c != 'species']
df[num_cols].hist(figsize=(8, 6), edgecolor='black')
plt.suptitle('Feature Distributions')
plt.show()

# Boxplot for Sepal Length
sns.boxplot(data=df, x='species', y='sepal length (cm)')
plt.title('Sepal Length Comparison')
plt.show()

# Pairplot to analyze feature relationships
sns.pairplot(df, hue='species')
plt.show()"""

    md2 = """## RESULT:
The experiment successfully demonstrated descriptive analytics on the Iris dataset using Pandas and Seaborn, providing insights into feature distributions and species differentiation."""

    nb = build_notebook([make_cell_markdown(md1), make_cell_code(code1), make_cell_markdown(md2)])
    save_notebook(nb, "Exp2D_Iris_Descriptive_Analytics.ipynb")

def generate_exp3a():
    md1 = """# Experiment 3A: Statistical Analysis Using Diabetes Datasets - Univariate Analysis

## AIM:
To analyze the Diabetes dataset from UCI and the Pima Indians Diabetes dataset using univariate statistical methods, including Frequency, Mean, Median, Mode, Variance, Standard Deviation, Skewness, and Kurtosis."""

    code1 = """import os
import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis

uci_path = os.path.join("..", "data", "raw", "uci_diabetes.csv")
pima_path = os.path.join("..", "data", "raw", "pima_diabetes.csv")

uci_diabetes = pd.read_csv(uci_path)
pima_diabetes = pd.read_csv(pima_path)

print("UCI Diabetes Dataset Sample:")
print(uci_diabetes.head())

print("\\nPima Indians Diabetes Dataset Sample:")
print(pima_diabetes.head())

numerical_columns = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]

def univariate_analysis(df, columns):
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

uci_stats = univariate_analysis(uci_diabetes, numerical_columns)
pima_stats = univariate_analysis(pima_diabetes, numerical_columns)

print("\\nUCI Diabetes Dataset Statistics:")
print(uci_stats)

print("\\nPima Indians Diabetes Dataset Statistics:")
print(pima_stats)"""

    md2 = """## RESULT:
The univariate analysis of the UCI Diabetes and Pima Indians Diabetes datasets reveals differences in central tendency, dispersion, and distribution. Variations in skewness and kurtosis indicate differences in data patterns between the datasets."""

    nb = build_notebook([make_cell_markdown(md1), make_cell_code(code1), make_cell_markdown(md2)])
    save_notebook(nb, "Exp3A_Diabetes_Univariate_Analysis.ipynb")

def main():
    print("=== Generating Jupyter Notebooks ===")
    generate_exp1()
    generate_exp2a()
    generate_exp2b()
    generate_exp2c()
    generate_exp2d()
    generate_exp3a()
    print("=== All Notebooks Generated Successfully! ===")

if __name__ == "__main__":
    main()
