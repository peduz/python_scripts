import numpy as np

def multiply_matrix_matrix(matrix1, matrix2):
    return np.matmul(matrix1, matrix2)

n_rows = int(input("Enter the number of rows for the first matrix: "))
n_cols = int(input("Enter the number of columns for the first matrix: "))

n_rows2 = int(input("Enter the number of rows for the second matrix: "))
n_cols2 = int(input("Enter the number of columns for the second matrix: "))

matrix1 = input("Enter the elements of the first matrix (separated by spaces): ").split()
matrix1 = [float(x) for x in matrix1]

matrix1 = np.array(matrix1).reshape(n_rows, n_cols)

matrix2 = input("Enter the elements of the second matrix (separated by spaces): ").split()
matrix2 = [float(x) for x in matrix2]
matrix2 = np.array(matrix2).reshape(n_rows2, n_cols2)

result = multiply_matrix_matrix(matrix1, matrix2)
print("Result of matrix multiplication:", result)