from sympy import *
import numpy as np
A = Matrix([[1, 1, 1],
     [3, 2, 1],
     [2, 1, 2]]
)
# Get REF
REF = A.echelon_form()

print(np.array(REF))

# Get RREF
RREF = A.rref()[0]

print(np.array(RREF))