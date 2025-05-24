#!/usr/bin/env python3
def matrix_shape(matrix):
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        if len(matrix) == 0:
            break
        matrix = matrix[0]
    return shape


print(matrix_shape([[2, 3, 4], [4, 5, 6]]))
