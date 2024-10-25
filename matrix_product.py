def matrix_product(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


#Input value of matrix
matrix1 = [[0, 1], [-1, 0]]
matrix2 = [[1, 1], [0, 1]]

res = matrix_product(matrix1, matrix2)

print("Product of matrix 1 and matrix 2: ", res)