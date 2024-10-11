import pandas as pd
import numpy as np
import sys

def is_number(s):
    try:
        # Try to convert the string to a number (float)
        float(s)
        return True
    except ValueError:
        # If there is an error, it's not a valid number
        return False

print("Change vector translating into orthogonal basis:")

print("Insert vector to translate values. Write 'end' to stop insertion")

# Input the vector v
x = []
a = input()
while a != "end":
    if a == "end":
        break
    elif is_number(a):
        x.append(float(a))
    else:
        print("Insert a number or 'end' to stop insertion")
    a = input()

if len(x) == 0:
    print("No values inserted")
    sys.exit()

v = np.array(x)
print("Vector v:", v)

# Construct the matrix of bases
basises = []

for basis_number in range(len(v)):
    basis = []
    print(f"Basis number {basis_number + 1} of {len(v)}")
    for i in range(len(v)):
        a = input(f"Insert coordinate {i + 1}: ")
        while not is_number(a):
            print("Insert a valid number")
            a = input(f"Insert coordinate {i + 1}: ")
        basis.append(float(a))
    
    basises.append(basis)

basises = np.array(basises).T  # Bases must be columns
print("Matrix of bases (columns are bases):\n", basises)

# Validate orthogonality
print("Check if all bases are orthogonal")
for i in range(basises.shape[1]):
    for j in range(i + 1, basises.shape[1]):
        dot_product = np.dot(basises[:, i], basises[:, j])
        if dot_product != 0:
            print(f"Bases {i + 1} and {j + 1} are not orthogonal. Dot product: {dot_product}")
            sys.exit()

print("All bases are orthogonal")

# Change of basis
print("Changing basis of vector v into coordinates defined by all bases")

# Matrix B with bases as columns (already set correctly)
B = basises

# Calculate the inverse of B
try:
    B_inv = np.linalg.inv(B)
except np.linalg.LinAlgError:
    print("Matrix of bases is not invertible.")
    sys.exit()

# Multiply the inverse of B by the vector v
alpha = np.dot(B_inv, v)

# Print the result
print("Vector in the new basis:", alpha)