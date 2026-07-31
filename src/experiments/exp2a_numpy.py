"""
Experiment 2A: Data Handling and Analysis - Working with NumPy Arrays
Aim: To understand and implement various NumPy operations, including array creation, indexing, slicing,
element-wise operations, aggregations, boolean operations, fancy indexing, reshaping, and structured arrays.
"""

import numpy as np

def run_experiment_2a():
    print("==================================================")
    print("EXPERIMENT 2A: WORKING WITH NUMPY ARRAYS")
    print("==================================================")

    # Check NumPy version
    print(f"NumPy Version: {np.__version__}")

    # Creating different types of arrays
    arr_1d = np.array([1, 2, 3, 4, 5])
    arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
    arr_0d = np.array(42)
    arr_ones = np.ones((3, 3))

    print("\n[+] Created Arrays:")
    print("1D Array:", arr_1d)
    print("2D Array:\n", arr_2d)
    print("0D Array:", arr_0d)
    print("Ones Array (3x3):\n", arr_ones)

    # Indexing and Slicing
    print("\n[+] Indexing and Slicing:")
    print("Element at index 2 in 1D array:", arr_1d[2])
    print("Element at row 1, column 2 in 2D array:", arr_2d[1, 2])
    print("Slice from 1D array (index 1 to 4):", arr_1d[1:4])
    print("Slice row 1 from 2D array:", arr_2d[1, :])

    # Element-wise operations
    arr_a = np.array([10, 20, 30])
    arr_b = np.array([1, 2, 3])

    print("\n[+] Element-wise Operations:")
    print("Array A:", arr_a)
    print("Array B:", arr_b)
    print("Addition:", arr_a + arr_b)
    print("Subtraction:", arr_a - arr_b)
    print("Multiplication:", arr_a * arr_b)
    print("Division:", arr_a / arr_b)
    print("Scalar Multiplication:", arr_a * 2)

    # Aggregations
    print("\n[+] Aggregations on Array A:")
    print("Sum:", np.sum(arr_a))
    print("Mean:", np.mean(arr_a))
    print("Standard Deviation:", np.std(arr_a))

    # Element-wise comparison
    print("\n[+] Comparison Operations:")
    print("Element-wise comparison (arr_a > arr_b):", arr_a > arr_b)

    # Boolean masking
    print("\n[+] Boolean Masking:")
    print("Elements greater than 15 in arr_a:", arr_a[arr_a > 15])

    # Fancy Indexing
    indices = [0, 2]
    print("\n[+] Fancy Indexing:")
    print(f"Selected elements at indices {indices}:", arr_a[indices])

    # Reshape
    reshaped_arr = arr_1d.reshape(5, 1)
    print("\n[+] Reshape:")
    print("Reshaped 1D array (5,) to 2D (5, 1):\n", reshaped_arr)

    # Structured Array
    structured_arr = np.array([(25, 90.5), (30, 85.2)], dtype=[('age', 'i4'), ('score', 'f4')])
    print("\n[+] Structured Array:")
    print("Structured array:", structured_arr)
    print("Ages:", structured_arr['age'])
    print("Scores:", structured_arr['score'])

    print("\nRESULT: Various NumPy operations, including array manipulations, indexing, slicing, arithmetic, aggregations, boolean masking, fancy indexing, reshaping, and structured arrays successfully executed.")

if __name__ == "__main__":
    run_experiment_2a()
