#!/usr/bin/env python3
"""Module for concatenating two arrays."""


def cat_arrays(arr1, arr2):
    """Concatenates two arrays.

    Args:
        arr1 (list of int/float): First array.
        arr2 (list of int/float): Second array.

    Returns:
        list: New list containing elements from both arrays.
    """
    return arr1 + arr2


print(cat_arrays([1, 2, 3], [4, 5, 6]))