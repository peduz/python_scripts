import numpy as np

print("Inserisci i vettori di input per verificare che siano linearmente indipendenti")

vector_number = input("Insert the number of vectors: ")

matrix = []
for i in range(int(vector_number)):
    v = input("Insert coordinates comma separated for the vector: ").split(',')
    v = [float(i) for i in v]
    matrix.append(v)

print(matrix)
matrix = np.array(matrix).T

determinant = np.linalg.det(matrix)

if determinant == 0:
    print("Vectors are linealy dependent")
else:
    print("Vectors are linealy independent")