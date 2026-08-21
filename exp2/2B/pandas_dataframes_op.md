# Pandas Dataframes — Output

Console output of `pandas_dataframes.py`.

```text
--- First 5 rows ---
   existing_column  another_column category_column  numeric_column  column1  column2
0             40.0              30               A             100       25     90.5
1             60.0              50               B             200       30     85.2
2             80.0              70               A             150       22     92.0
3             20.0              90               B             300       35     78.0
4             90.0             110               A             250       28     88.4

--- Last 5 rows ---
   existing_column  another_column category_column  numeric_column  column1  column2
3             20.0              90               B             300       35     78.0
4             90.0             110               A             250       28     88.4
5             55.0              85               B             180       31     91.0
6             75.0              45               A             220       27     86.5
7              NaN              60               B             270       29     89.0

--- DataFrame Info ---
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 8 entries, 0 to 7
Data columns (total 6 columns):
 #   Column           Non-Null Count  Dtype  
---  ------           --------------  -----  
 0   existing_column  7 non-null      float64
 1   another_column   8 non-null      int64  
 2   category_column  8 non-null      object 
 3   numeric_column   8 non-null      int64  
 4   column1          8 non-null      int64  
 5   column2          8 non-null      float64
dtypes: float64(2), int64(3), object(1)
memory usage: 516.0+ bytes

--- Summary Statistics ---
       existing_column  another_column  numeric_column    column1    column2
count         7.000000        8.000000        8.000000   8.000000   8.000000
mean         60.000000       67.500000      208.750000  28.375000  87.575000
std          24.324199       26.457513       65.560768   3.925648   4.488955
min          20.000000       30.000000      100.000000  22.000000  78.000000
25%          47.500000       48.750000      172.500000  26.500000  86.175000
50%          60.000000       65.000000      210.000000  28.500000  88.700000
75%          77.500000       86.250000      255.000000  30.250000  90.625000
max          90.000000      110.000000      300.000000  35.000000  92.000000

--- Series Addition ---
0     50.0
1     70.0
2     90.0
3     30.0
4    100.0
5     65.0
6     85.0
7     70.0
Name: existing_column, dtype: float64

--- Filtered DataFrame ---
   existing_column  another_column category_column  numeric_column  column1  column2  new_column
1             60.0              50               B             200       30     85.2       120.0
2             80.0              70               A             150       22     92.0       160.0
5             55.0              85               B             180       31     91.0       110.0
6             75.0              45               A             220       27     86.5       150.0
7             60.0              60               B             270       29     89.0       120.0

--- Grouped Mean ---
category_column
A    180.0
B    237.5
Name: numeric_column, dtype: float64

--- Sorted DataFrame ---
   existing_column  another_column category_column  numeric_column  column1  column2  new_column
3             20.0              90               B             300       35     78.0        40.0
7             60.0              60               B             270       29     89.0       120.0
4             90.0             110               A             250       28     88.4       180.0
6             75.0              45               A             220       27     86.5       150.0
1             60.0              50               B             200       30     85.2       120.0
5             55.0              85               B             180       31     91.0       110.0
2             80.0              70               A             150       22     92.0       160.0
0             40.0              30               A             100       25     90.5        80.0

--- Masked DataFrame ---
   existing_column  another_column category_column  numeric_column  column1  column2  new_column
3             20.0              90               B             300       35     78.0        40.0
4             90.0             110               A             250       28     88.4       180.0
6             75.0              45               A             220       27     86.5       150.0
7             60.0              60               B             270       29     89.0       120.0

Saved subset DataFrame to 'filtered_data.csv'

--- Final Aggregations ---
Total sum: 1670
Mean: 208.75
Standard Deviation: 65.56076788533127
```
