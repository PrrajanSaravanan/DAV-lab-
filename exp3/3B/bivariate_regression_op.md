# Bivariate Regression — Output

Console output of `bivariate_regression.py`.

```text
UCI Diabetes Dataset Sample:
   Glucose  BloodPressure  SkinThickness  Insulin        BMI  DiabetesPedigreeFunction  Age  Outcome
0       90             72             16      264  22.273511                  1.162896   79        0
1      162             61             34      143  41.814986                  2.158993   35        0
2      184             76             25      128  36.309833                  1.411238   31        0
3      119             83             20      230  27.258685                  1.202206   28        1
4      175            101             30       63  41.493982                  0.214888   59        1

Pima Indians Diabetes Dataset Sample:
   Glucose  BloodPressure  SkinThickness  Insulin        BMI  DiabetesPedigreeFunction  Age  Outcome
0       81             97             15      289  27.062801                  0.797425   62        1
1      172             50             24      229  18.588741                  0.652107   21        1
2       90             84             40      136  32.968461                  0.952396   29        0
3      187             94             30      288  38.217097                  1.036946   35        1
4      133             94             46       23  37.236422                  1.494192   62        0

Linear Regression (UCI Diabetes - Predicting BMI using Glucose):
R2 Score: 0.5781
Saved plot to 'uci_linear_regression.png'

Linear Regression (Pima Indians Diabetes - Predicting BMI using Glucose):
R2 Score: 0.6159
Saved plot to 'pima_linear_regression.png'

Logistic Regression (UCI Diabetes - Predicting Outcome using ['Glucose', 'BloodPressure', 'BMI', 'Age']):
Accuracy Score: 0.6000

Logistic Regression (Pima Indians Diabetes - Predicting Outcome using ['Glucose', 'BloodPressure', 'BMI', 'Age']):
Accuracy Score: 0.5000
```
