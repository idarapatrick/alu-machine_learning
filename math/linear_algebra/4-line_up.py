
import numpy as np


def add_arrays(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)

    if len(arr1) == len(arr2):
        return arr1 + arr2
    else:
        return None


print(add_arrays([1, 2, 3], [4, 5, 6]))
