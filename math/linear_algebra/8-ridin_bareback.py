#!/usr/bin/env python3
"""Module for matrix multiplication."""


def mat_mul(mat1, mat2):
    """Performs matrix multiplication of two 2D matrices.

    Args:
        mat1 (list of lists): First 2D matrix.
        mat2 (list of lists): Second 2D matrix.

    Returns:
        list of lists: New matrix resulting from multiplication if possible, else None.
    """
    # Number of columns in mat1 must be equal to number of rows in mat2
    if len(mat1[0]) != len(mat2):
        return None

    result = []
    i = 0
    while i < len(mat1):
        row = []
        j = 0
        while j < len(mat2[0]):
            sum_val = 0
            k = 0
            while k < len(mat2):
                sum_val += mat1[i][k] * mat2[k][j]
                k += 1
            row.append(sum_val)
            j += 1
        result.append(row)
        i += 1

    return result
