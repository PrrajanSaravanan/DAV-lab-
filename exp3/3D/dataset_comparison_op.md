# Dataset Comparison — Output

Console output of `dataset_comparison.py`.

```text
Comparison of Univariate Analysis Results:

UCI Diabetes Dataset Statistics:
                     Mean      Median     Variance  Standard Deviation  Skewness  Kurtosis
Glucose        137.310000  136.000000  1271.812020           35.662474 -0.247083  0.022131
BloodPressure   82.900000   82.500000   374.656566           19.356047  0.401491  0.129440
BMI             30.947785   31.008247    60.624589            7.786179  0.233861 -0.130391

Pima Indians Diabetes Dataset Statistics:
                     Mean      Median     Variance  Standard Deviation  Skewness  Kurtosis
Glucose        136.590000  135.500000  1014.385758           31.849423  0.268308  0.021330
BloodPressure   81.900000   82.500000   426.717172           20.657134  0.211310 -0.075294
BMI             32.458588   32.786506    47.887400            6.920072 -0.421524 -0.109505

--- Model Performance Comparison ---
Multiple Regression R2 Scores: UCI - 0.9464, Pima - 0.7068
Logistic Regression Accuracy: UCI - 60.0%, Pima - 50.0%

Higher multiple regression R2 score: UCI Diabetes dataset.
```
