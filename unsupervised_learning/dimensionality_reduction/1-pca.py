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

    # Compute the covariance matrix
    # Cov = (1/n) * X_m^T @ X_m
    n = X.shape[0]
    cov_matrix = np.matmul(X_m.T, X_m) / n

    # Compute eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

    # Sort eigenvalues and eigenvectors in descending order
    idx = eigenvalues.argsort()[::-1]
    eigenvectors = eigenvectors[:, idx]

    # Select the top ndim eigenvectors as the weight matrix
    W = eigenvectors[:, :ndim]

    # Transform the centered data
    T = np.matmul(X_m, W)

    return T
