#!/usr/bin/env python3
import numpy as np 


def add_matrices2D(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None

    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)


mat1 = [[1, 2], [3, 4]]
mat2 = [[2, 4], [2, 5]]
print(add_matrices2D(mat1, mat2))
