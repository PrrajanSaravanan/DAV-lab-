# CS4503 — Data Analytics and Visualization Lab

Lab experiments for CS4503, Chennai Institute of Technology.

Each experiment has its own folder. Experiments with sub-parts (A, B, C, D) have one
sub-folder each, holding that part's script, notebook, datasets, and generated plots.

## Experiments

| # | Category | Sub-experiments |
|---|----------|-----------------|
| 1 | Installation and Exploration | — |
| 2 | Data Handling and Analysis | A) NumPy arrays · B) Pandas DataFrames · C) Reading text/Excel/web · D) Iris descriptive analytics |
| 3 | Statistical Analysis (Diabetes) | A) Univariate · B) Bivariate regression · C) Multiple regression · D) Dataset comparison |
| 4 | Visualization and Hypothesis Testing | A) Normal curves · B) Z-test · C) T-test · D) ANOVA |
| 5 | Model Building and Validation | A) Linear models · B) Logistic models · C) Time series analysis |

## Structure

```
exp1/                          Installation and exploration
exp2/  2A/ 2B/ 2C/ 2D/         Data handling and analysis
exp3/  3A/ 3B/ 3C/ 3D/         Statistical analysis using diabetes datasets
exp4/  4A/ 4B/ 4C/ 4D/         Visualization and hypothesis testing
exp5/  5A/ 5B/ 5C/             Model building and validation
```

## Datasets

- **UCI Diabetes** and **Pima Indians Diabetes** — 100 records each, 8 columns
  (Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age, Outcome).
  Used by experiments 3, 4, and 5.
- **Iris** — 150 records, used by 2D.
- **Google Play data** and a sample Excel workbook — used by 2B and 2C.

Each folder holds its own copy of the datasets it needs, so every script runs on its own.

## Running

Install the packages:

```bash
pip install numpy scipy pandas matplotlib seaborn statsmodels scikit-learn openpyxl jupyterlab
```

Run any experiment directly:

```bash
python exp3/3A/univariate_analysis.py
```

Or open the matching `.ipynb` in Jupyter. Scripts save their plots as PNG files
into the same folder.

## Note on experiment 5C

The lab manual runs the time series analysis on a 768-record dataset with a seasonal
period of 30. That file is not in this repository, so 5C uses the 100-record UCI glucose
series with a period of 12. The datasets have no timestamp column, so the record index
serves as the time axis.
