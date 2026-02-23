#!/usr/bin/env python3
"""Module for PCA."""
import numpy as np


def pca(X, ndim):
    """Performs PCA on a dataset.

    Args:
        X: numpy.ndarray of shape (n, d) where n is number of data points
           and d is number of dimensions
        ndim: new dimensionality of the transformed X

    Returns:
        T: numpy.ndarray of shape (n, ndim) containing the transformed
           version of X
    """
    # Center the data by subtracting the mean
    X_m = X - np.mean(X, axis=0)

    # Perform SVD on the centered data matrix
    # X_m = U * S * V^T
    # The columns of V are the principal components
    U, S, Vt = np.linalg.svd(X_m, full_matrices=False)

    # V^T rows are the principal components, we need V columns
    # Select the top ndim eigenvectors as the weight matrix
    W = Vt.T[:, :ndim]

    # Transform the centered data
    T = np.matmul(X_m, W)

    return T
