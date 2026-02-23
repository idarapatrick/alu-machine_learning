#!/usr/bin/env python3
"""Module for performing PCA on a dataset to a specified dimensionality."""
import numpy as np


def pca(X, ndim):
    """Perform PCA on a dataset reducing it to ndim dimensions.

    Args:
        X: numpy.ndarray of shape (n, d) containing the dataset
        ndim: new dimensionality of the transformed X

    Returns:
        T: numpy.ndarray of shape (n, ndim) containing the transformed X
    """
    X_m = X - np.mean(X, axis=0)
    _, _, Vt = np.linalg.svd(X_m)
    W = Vt[:ndim].T
    return np.matmul(X_m, W)
