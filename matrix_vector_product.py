import numpy as np

def multiply_matrix_and_vector(matrix: np.matrix, vector: np.array):
    return matrix.dot(vector)

v = input("Enter the vector: ").split(",")
vector = [int(x) for x in v]

n_row = input("Insert how many rows the matrix has: ")
n_col = input("Insert how many columns the matrix has: ")


matrix_values = input("Enter the matrix values separated by commas: ").split(",")
matrix_values = [float(x) for x in matrix_values]
    
matrix_values = np.array(matrix_values)

matrix = matrix_values.reshape(int(n_row), int(n_col))
print("Matrix: ", matrix)
res = multiply_matrix_and_vector(matrix, np.array(vector))
print("Result: ", res)