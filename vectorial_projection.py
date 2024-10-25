import numpy as np
import sys

def scalar_product(v1, v2):
    return np.dot(v1, v2)


def vector_projection(v1, v2):
    return (scalar_product(v1, v2) / scalar_product(v2, v2)) * v2


v = input("Insert the vector coordinates comma separated: ").split(',')
v = [float(i) for i in v]

c = input("Insert the projection vector: ").split(',')
c = [float(i) for i in c]

projc_v = vector_projection(np.array(v), np.array(c))

print("The vector projection is:", projc_v)