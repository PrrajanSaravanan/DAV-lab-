<<<<<<< HEAD
<div align="center">

# 📊 Data Analysis & Visualization Lab

### 🏫 Chennai Institute of Technology — Semester 5

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![NumPy](https://img.shields.io/badge/NumPy-2.2.6-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org)
[![Pandas](https://img.shields.io/badge/Pandas-2.3.3-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.10.3-11557C?style=for-the-badge)](https://matplotlib.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Lab_4.5.1-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)

---

> _A comprehensive collection of hands-on laboratory experiments exploring data analysis,  
> manipulation, and visualization using Python's scientific computing ecosystem._

</div>

---

## 🗂️ Repository Structure

```
DAV_LAB/
│
├── 📁 exp1/
│   ├── 📓 exp1.ipynb        ← Jupyter Notebook
│   └── 🐍 exp1.py           ← Python Script
│
├── 📁 exp2/
│   ├── 📓 exp2.ipynb        ← Jupyter Notebook (with outputs)
│   └── 🐍 exp2.py           ← Python Script
│
├── 📁 exp3/
│   ├── 📊 data.csv          ← Sample Dataset
│   ├── 📓 exp3.ipynb        ← Jupyter Notebook (with outputs)
│   └── 🐍 exp3.py           ← Python Script
│
├── 📁 exp4/
│   ├── 📊 Google_data (2b.c1).csv  ← Text/CSV Dataset
│   ├── 📊 data (2c2).xlsx          ← Excel Spreadsheet Dataset
│   ├── 📓 exp4.ipynb               ← Jupyter Notebook (with outputs)
│   ├── 🐍 exp4.py                  ← Python Script
│   ├── 📄 processed_text.csv       ← Exported Processed CSV
│   └── 📄 processed_excel.xlsx     ← Exported Processed Excel
│
├── 📁 exp5/
│   ├── 📊 iris_dataset(2d).csv     ← Iris CSV Dataset
│   ├── 📓 exp5.ipynb               ← Jupyter Notebook (with outputs)
│   ├── 🐍 exp5.py                  ← Python Script
│   ├── 🖼️ histograms.png            ← Feature Distributions Plot
│   ├── 🖼️ sepal_length_boxplot.png  ← Sepal Length Boxplot
│   └── 🖼️ pairplot.png              ← Feature Pairwise Scatter/KDE Plot
│
├── 📁 exp6/
│   ├── 📊 uci_diabetes.csv         ← UCI Diabetes Dataset
│   ├── 📊 pima_diabetes.csv        ← Pima Indians Diabetes Dataset
│   ├── 📓 exp6.ipynb               ← Jupyter Notebook (with outputs)
│   └── 🐍 exp6.py                  ← Python Script
│
├── 📁 exp7/
│   ├── 📊 uci_diabetes.csv         ← UCI Diabetes Dataset
│   ├── 📊 pima_diabetes.csv        ← Pima Indians Diabetes Dataset
│   ├── 📓 exp7.ipynb               ← Jupyter Notebook (with outputs)
│   ├── 🐍 exp7.py                  ← Python Script
│   ├── 🖼️ uci_linear_regression.png ← UCI Linear Regression Scatter & Line Plot
│   └── 🖼️ pima_linear_regression.png ← Pima Linear Regression Scatter & Line Plot
│
└── 📄 README.md
```

---

## 🧪 Experiments at a Glance

| # | Experiment | Description | Key Libraries |
|:-:|:-----------|:------------|:-------------:|
| 1 | **Environment Setup** | Verify installation & versions of essential data science packages | `numpy` `pandas` `matplotlib` `jupyter` |
| 2 | **NumPy Fundamentals** | Core array operations — creation, indexing, slicing, math, reshaping | `numpy` |
| 3 | **Pandas Data Analysis** | DataFrame manipulation — loading, cleaning, filtering, grouping, exporting | `pandas` |
| 4 | **Data Input/Output Operations** | Reading data from CSV, Excel, and Web; missing value treatment; exporting | `pandas` `openpyxl` |
| 5 | **Descriptive Analytics (Iris)** | Exploring statistics, distributions, boxplots, and pairplots on Iris dataset | `pandas` `seaborn` `matplotlib` |
| 6 | **Univariate Statistical Analysis** | Calculating Mean, Median, Mode, Variance, Std, Skewness, Kurtosis on Diabetes datasets | `pandas` `numpy` `scipy` |
| 7 | **Bivariate Analysis (Linear & Logistic Regression)** | Linear Regression (Glucose vs BMI) & Logistic Regression (Predicting Diabetes) | `pandas` `numpy` `scikit-learn` `matplotlib` |

---

## 📝 Detailed Experiment Breakdown

<details>
<summary><strong>🔬 Experiment 1 — Environment Setup & Package Verification</strong></summary>

### 📌 Objective
Verify the installation and versions of all essential data science libraries required for the lab.

### 📦 Packages Checked

| Package | Status | Version |
|:--------|:------:|:-------:|
| NumPy | ✅ Installed | `2.2.6` |
| Pandas | ✅ Installed | `2.3.3` |
| Matplotlib | ✅ Installed | `3.10.3` |
| JupyterLab | ✅ Installed | `4.5.1` |
| Seaborn | ❌ Not Installed | — |
| SciPy | ❌ Not Installed | — |
| Plotly | ❌ Not Installed | — |
| Bokeh | ❌ Not Installed | — |
| Statsmodels | ❌ Not Installed | — |

### 📂 Files
- [`exp1/exp1.ipynb`](exp1/exp1.ipynb) — Jupyter Notebook
- [`exp1/exp1.py`](exp1/exp1.py) — Python Script

</details>

---

<details>
<summary><strong>🔬 Experiment 2 — Fundamentals of NumPy</strong></summary>

### 📌 Objective
Learn and demonstrate core NumPy operations for numerical computing.

### 🧩 Topics Covered

| Section | Topic | Key Functions |
|:-------:|:------|:-------------|
| 1 | Version Verification | `np.__version__` |
| 2 | Array Creation | `np.array()`, `np.ones()` |
| 3 | Indexing & Slicing | `arr[i]`, `arr[start:end]`, `arr[row, col]` |
| 4 | Element-wise Operations | `+`, `-`, `*`, `/`, scalar math |
| 5 | Statistical Aggregations | `np.sum()`, `np.mean()`, `np.std()` |
| 6 | Comparison & Masking | `>`, boolean indexing, fancy indexing |
| 7 | Reshaping & Structured Arrays | `.reshape()`, structured `dtype` |

### 💡 Sample Output
```python
>>> arr_a = np.array([10, 20, 30])
>>> arr_b = np.array([1, 2, 3])
>>> print("Addition:", arr_a + arr_b)
Addition: [11 22 33]
```

### 📂 Files
- [`exp2/exp2.ipynb`](exp2/exp2.ipynb) — Jupyter Notebook (with cell outputs)
- [`exp2/exp2.py`](exp2/exp2.py) — Python Script

</details>

---

<details>
<summary><strong>🔬 Experiment 3 — Data Analysis & Manipulation using Pandas</strong></summary>

### 📌 Objective
Perform real-world data analysis workflows using Pandas DataFrames.

### 🧩 Topics Covered

| Section | Topic | Key Functions |
|:-------:|:------|:-------------|
| 1 | Load & Preview | `pd.read_csv()`, `.head()`, `.tail()` |
| 2 | Inspection | `.info()`, `.describe()` |
| 3 | Missing Values & Column Ops | `.fillna()`, column arithmetic |
| 4 | Filtering & Groupby | Boolean conditions, `.groupby().mean()` |
| 5 | Sorting & Boolean Masking | `.sort_values()`, `.median()` masking |
| 6 | Export & Aggregations | `.to_csv()`, `.sum()`, `.mean()`, `.std()` |

### 💡 Sample Output
```python
>>> grouped = df.groupby('category_column')['numeric_column'].mean()
>>> print(grouped)
category_column
A    180.0
B    237.5
Name: numeric_column, dtype: float64
```

### 📂 Files
- [`exp3/exp3.ipynb`](exp3/exp3.ipynb) — Jupyter Notebook (with cell outputs)
- [`exp3/exp3.py`](exp3/exp3.py) — Python Script
- [`exp3/data.csv`](exp3/data.csv) — Sample Dataset

</details>

---

<details>
<summary><strong>🔬 Experiment 4 — Reading Data from Text Files, Excel, and the Web</strong></summary>

### 📌 Objective
Read and process data from various sources, including CSV text files, Excel spreadsheets, and web-based URLs using Pandas.

### 🧩 Topics Covered

| Section | Topic | Key Functions |
|:-------:|:------|:-------------|
| 1 | Read CSV / Text Data | `pd.read_csv('Google_data (2b.c1).csv')` |
| 2 | Read Excel Data | `pd.read_excel('data (2c2).xlsx', sheet_name='Sheet1')` |
| 3 | Read Web-Based Data | `pd.read_csv('https://raw.githubusercontent.com/...')` |
| 4 | Preview Datasets | `df.head()` |
| 5 | Handle Missing Values | `.ffill()`, `.bfill()`, `.dropna()` |
| 6 | Export Processed Data | `.to_csv('processed_text.csv')`, `.to_excel('processed_excel.xlsx')` |

### 💡 Sample Code & Output
```python
import pandas as pd

text_df = pd.read_csv('Google_data (2b.c1).csv')
excel_df = pd.read_excel('data (2c2).xlsx', sheet_name='Sheet1')
web_df = pd.read_csv('https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv')

print(text_df.head(), "\n", excel_df.head(), "\n", web_df.head())
```

### 📂 Files
- [`exp4/exp4.ipynb`](exp4/exp4.ipynb) — Jupyter Notebook (with cell outputs)
- [`exp4/exp4.py`](exp4/exp4.py) — Python Script
- [`exp4/Google_data (2b.c1).csv`](exp4/Google_data%20%282b.c1%29.csv) — CSV Dataset
- [`exp4/data (2c2).xlsx`](exp4/data%20%282c2%29.xlsx) — Excel Dataset
- [`exp4/processed_text.csv`](exp4/processed_text.csv) — Exported CSV Data
- [`exp4/processed_excel.xlsx`](exp4/processed_excel.xlsx) — Exported Excel Data

</details>

---

<details>
<summary><strong>🔬 Experiment 5 — Exploring Descriptive Analytics Using the Iris Dataset</strong></summary>

### 📌 Objective
Perform descriptive analytics, summary statistics, univariate, and bivariate visualizations on the Iris dataset using Pandas, Seaborn, and Matplotlib.

### 🧩 Topics Covered

| Section | Topic | Key Functions |
|:-------:|:------|:-------------|
| 1 | Dataset Load & Preview | `pd.read_csv('iris_dataset(2d).csv')` |
| 2 | Basic Info & Statistics | `df.info()`, `df.describe()` |
| 3 | Univariate Analysis | `df['species'].value_counts()` |
| 4 | Distribution Plots | `df.hist(figsize=(8, 6), edgecolor='black')` |
| 5 | Boxplot Analysis | `sns.boxplot(data=df, x='species', y='sepal length (cm)')` |
| 6 | Pair Plot Visualizations | `sns.pairplot(df, hue='species')` |

### 💡 Sample Code & Output
```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('iris_dataset(2d).csv')
print(df.info())
print(df.describe())

sns.boxplot(data=df, x='species', y='sepal length (cm)')
sns.pairplot(df, hue='species')
```

### 📂 Files
- [`exp5/exp5.ipynb`](exp5/exp5.ipynb) — Jupyter Notebook (with cell outputs)
- [`exp5/exp5.py`](exp5/exp5.py) — Python Script
- [`exp5/iris_dataset(2d).csv`](exp5/iris_dataset%282d%29.csv) — Iris Dataset
- [`exp5/histograms.png`](exp5/histograms.png) — Feature Distribution Plot
- [`exp5/sepal_length_boxplot.png`](exp5/sepal_length_boxplot.png) — Boxplot
- [`exp5/pairplot.png`](exp5/pairplot.png) — Pairwise Plot

</details>

---

<details>
<summary><strong>🔬 Experiment 6 — Statistical Analysis Using Diabetes Datasets (Univariate Analysis)</strong></summary>

### 📌 Objective
Perform univariate statistical analysis on the UCI Diabetes and Pima Indians Diabetes datasets to compute central tendency, dispersion, skewness, and kurtosis.

### 🧩 Topics Covered

| Section | Topic | Key Functions / Metrics |
|:-------:|:------|:-----------------------|
| 1 | Import Datasets | `pd.read_csv('uci_diabetes.csv')`, `pd.read_csv('pima_diabetes.csv')` |
| 2 | Central Tendency | `np.mean()`, `np.median()`, `df[col].mode()[0]` |
| 3 | Dispersion | `np.var(ddof=1)`, `np.std(ddof=1)` |
| 4 | Shape & Tail Metrics | `scipy.stats.skew()`, `scipy.stats.kurtosis()` |
| 5 | Automated Analysis Pipeline | Custom function `univariate_analysis(df, columns)` |

### 💡 Sample Code & Output
```python
import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis

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
```

### 📂 Files
- [`exp6/exp6.ipynb`](exp6/exp6.ipynb) — Jupyter Notebook (with cell outputs)
- [`exp6/exp6.py`](exp6/exp6.py) — Python Script
- [`exp6/uci_diabetes.csv`](exp6/uci_diabetes.csv) — UCI Diabetes Dataset
- [`exp6/pima_diabetes.csv`](exp6/pima_diabetes.csv) — Pima Indians Diabetes Dataset

</details>

---

<details>
<summary><strong>🔬 Experiment 7 — Bivariate Analysis: Linear and Logistic Regression Modeling</strong></summary>

### 📌 Objective
Perform bivariate analysis on the UCI Diabetes Dataset and Pima Indians Diabetes Dataset using Linear Regression (continuous vs. continuous) and Logistic Regression (binary classification of diabetes presence).

### 🧩 Topics Covered

| Section | Topic | Key Functions / Metrics |
|:-------:|:------|:-----------------------|
| 1 | Load Datasets | `pd.read_csv('uci_diabetes.csv')`, `pd.read_csv('pima_diabetes.csv')` |
| 2 | Linear Regression | `LinearRegression()`, `.fit()`, `.predict()`, `r2_score()` |
| 3 | Regression Visualizations | `plt.scatter()`, `plt.plot()`, regression line plotting |
| 4 | Logistic Regression | `train_test_split()`, `LogisticRegression()`, `accuracy_score()` |
| 5 | Performance Comparison | Evaluating model performance across dataset variations |

### 💡 Sample Code & Output
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import r2_score, accuracy_score

# 1. Linear Regression (Glucose vs. BMI)
model_lin = LinearRegression().fit(df[['Glucose']], df['BMI'])
y_pred = model_lin.predict(df[['Glucose']])
print("R2 Score:", r2_score(df['BMI'], y_pred))

# 2. Logistic Regression (Outcome prediction)
X_train, X_test, y_train, y_test = train_test_split(df[['Glucose', 'BloodPressure', 'BMI', 'Age']], df['Outcome'], test_size=0.2, random_state=42)
model_log = LogisticRegression().fit(X_train, y_train)
print("Accuracy Score:", accuracy_score(y_test, model_log.predict(X_test)))
```

### 📂 Files
- [`exp7/exp7.ipynb`](exp7/exp7.ipynb) — Jupyter Notebook (with cell outputs & plots)
- [`exp7/exp7.py`](exp7/exp7.py) — Python Script
- [`exp7/uci_diabetes.csv`](exp7/uci_diabetes.csv) — UCI Diabetes Dataset
- [`exp7/pima_diabetes.csv`](exp7/pima_diabetes.csv) — Pima Indians Diabetes Dataset
- [`exp7/uci_linear_regression.png`](exp7/uci_linear_regression.png) — UCI Scatter Plot & Linear Fit
- [`exp7/pima_linear_regression.png`](exp7/pima_linear_regression.png) — Pima Scatter Plot & Linear Fit

</details>

---

## 🚀 Getting Started

### Prerequisites

```bash
# Ensure Python 3.x is installed
python --version

# Install required packages
pip install numpy pandas matplotlib seaborn scipy scikit-learn jupyterlab
```

### Running Notebooks

```bash
# Clone the repository
git clone https://github.com/NareeshKannaS/DAV-LAB-EXP.git
cd DAV-LAB-EXP

# Launch Jupyter Lab
jupyter lab
```

### Running Python Scripts

```bash
# Example: Run Experiment 2
cd exp2
python exp3.py
```

---

## 🛠️ Tech Stack

<div align="center">

| Technology | Purpose |
|:----------:|:--------|
| 🐍 **Python 3.x** | Core programming language |
| 🔢 **NumPy** | Numerical computing & array operations |
| 🐼 **Pandas** | Data manipulation & analysis |
| 📈 **Matplotlib** | Data visualization & plotting |
| 📓 **Jupyter Lab** | Interactive notebook environment |

</div>

---

## 📊 Learning Roadmap

```
 ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
 │   Exp 1      │     │   Exp 2      │     │   Exp 3      │
 │ Environment  │────▶│   NumPy      │────▶│   Pandas     │──▶ ...
 │   Setup      │     │ Fundamentals │     │  Analysis    │
 └──────────────┘     └──────────────┘     └──────────────┘
```

> [!NOTE]
> Each experiment builds upon concepts from the previous one. It is recommended to follow the experiments in order.

> [!TIP]
> All notebooks include pre-rendered cell outputs so you can review results without running the code.

---

<div align="center">

### ⭐ Star this repo if you found it helpful!

Made with ❤️ for **Data Analysis & Visualization Lab**

</div>
=======
# DAV-LAB-EXP
>>>>>>> f4a60fb126ce4a50d61afe94c5995a90c36c8569
