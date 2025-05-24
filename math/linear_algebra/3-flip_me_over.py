#!/usr/bin/env python3
def matrix_transpose(matrix):
    """Return the transpose of a 2D matrix."""
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


print(matrix_transpose([[2, 4, 3], [5, 8, 7]]))