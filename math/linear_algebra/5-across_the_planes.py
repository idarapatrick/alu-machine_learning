#!/usr/bin/env python3
import numpy as np 

import numpy as np

def add_matrices2D(mat1, mat2):
    """function to add two matrices element-wise"""

    mat1 = np.array(mat1)
    mat2 = np.array(mat2)
    if mat1.shape != mat2.shape:
        return None
    return mat1 + mat2

mat1 = [[1, 2], [3, 4]]
mat2 = [[2, 4], [2, 5]]
print(add_matrices2D(mat1, mat2))

print(mat1)
print(mat2)
print(add_matrices2D(mat1, [[1, 2, 3], [4, 5, 6]]))

