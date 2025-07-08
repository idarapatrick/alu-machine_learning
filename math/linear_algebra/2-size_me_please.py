#!/usr/bin/env python3
"""Module for calculating the shape of a matrix."""

def matrix_shape(matrix):
    """Calculates the shape of a matrix (nested lists).

    Args:
        matrix (list): A nested list representing the matrix.

    Returns:
        list: The shape of the matrix as a list of integers.
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        if len(matrix) == 0:
            break
        matrix = matrix[0]
    return shape
