#!/usr/bin/env python3
"""Module for element-wise operations on numpy.ndarrays."""

def np_elementwise(mat1, mat2):
    """Performs element-wise addition, subtraction, multiplication, and division.

    Args:
        mat1 (numpy.ndarray): First numpy array.
        mat2 (numpy.ndarray): Second numpy array.

    Returns:
        tuple: Tuple containing (sum, difference, product, quotient).
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
