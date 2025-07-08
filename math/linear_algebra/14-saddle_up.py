#!/usr/bin/env python3
"""Module for matrix multiplication using numpy."""

import numpy as np  # type: ignore


def np_matmul(mat1, mat2):
    """Performs matrix multiplication of two numpy.ndarrays.

    Args:
        mat1 (numpy.ndarray): First numpy array.
        mat2 (numpy.ndarray): Second numpy array.

    Returns:
        numpy.ndarray: The result of matrix multiplication.
    """
    return np.matmul(mat1, mat2)

