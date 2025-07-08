#!/usr/bin/env python3
"""Module for concatenating two 2D matrices along a specific axis."""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenates two 2D matrices along a specific axis.

    Args:
        mat1 (list of lists): First 2D matrix.
        mat2 (list of lists): Second 2D matrix.
        axis (int): Axis along which to concatenate (0 for rows, 1 for columns).

    Returns:
        list of lists: New concatenated matrix if possible, else None.
    """
    if axis == 0:
        if len(mat1) == 0 or len(mat2) == 0 or len(mat1[0]) != len(mat2[0]):
            return None
        result = []
        for row in mat1:
            result.append(row[:])
        for row in mat2:
            result.append(row[:])
        return result
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        result = []
        i = 0
        while i < len(mat1):
            result.append(mat1[i][:] + mat2[i][:])
            i += 1
        return result
    else:
        return None


mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6]]
mat3 = [[7], [8]]
mat4 = cat_matrices2D(mat1, mat2)
mat5 = cat_matrices2D(mat1, mat3, axis=1)
print(mat4)
print(mat5)
mat1[0] = [9, 10]
mat1[1].append(5)
print(mat1)
print(mat4)
print(mat5)
