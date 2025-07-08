#!/usr/bin/env python3
"""Module for element-wise addition of two arrays."""


def add_arrays(arr1, arr2):
    """Adds two arrays element-wise.

    Args:
        arr1 (list of int/float): First array.
        arr2 (list of int/float): Second array.

    Returns:
        list: New list with element-wise sums if shapes match, else None.
    """
    if len(arr1) != len(arr2):
        return None
    return [a + b for a, b in zip(arr1, arr2)]

