#!/usr/bin/env python3
"""Module for concatenating two numpy.ndarrays along a specific axis."""

import numpy as np  # type: ignore


def np_cat(mat1, mat2, axis=0):
    """Concatenates two numpy.ndarrays along a specific axis.

    Args:
        mat1 (numpy.ndarray): First numpy array.
        mat2 (numpy.ndarray): Second numpy array.
        axis (int): Axis along which to concatenate (default 0).

    Returns:
        numpy.ndarray: The concatenated array.
    """
    return np.concatenate((mat1, mat2), axis=axis)

