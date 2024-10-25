import numpy as np
import sys

print("Inserisci i vettori di input per verificare che siano linearmente indipendenti")

vector = input("Insert the vector coordinates comma separated: ").split(',')
vector = [float(i) for i in vector]

vector_number = input("Insert the number of vectors: ")

matrix = []
for i in range(int(vector_number)):
    v = input("Insert coordinates comma separated for the vector: ").split(',')
    v = [float(i) for i in v]
    matrix.append(v)


print(matrix)
matrix = np.array(matrix).T

#check if matrix is invertible
try:
    inv_matrix = np.linalg.inv(matrix)
except: #not invertible
    print("Matrix is not invertible")
    sys.exit()

q = np.dot(inv_matrix, vector)

print("The coordinate for vector dependency:", q)