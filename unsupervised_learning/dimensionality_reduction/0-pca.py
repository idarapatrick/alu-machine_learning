#!/usr/bin/env python3
"""Module for PCA."""
import numpy as np


def pca(X, var=0.95):
    """Performs PCA on a dataset.

    Args:
        X: numpy.ndarray of shape (n, d) where n is number of data points
           and d is number of dimensions, with mean 0 across all data points
        var: fraction of the variance that PCA should maintain

    Returns:
        W: numpy.ndarray of shape (d, nd) that maintains var fraction of
           X's original variance, where nd is the new dimensionality
    """
    # Compute covariance matrix (data already has mean 0)
    # Cov = (1/n) * X^T @ X
    n = X.shape[0]
    cov_matrix = np.matmul(X.T, X) / n

    # Compute eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

    # Sort eigenvalues and eigenvectors in descending order
    idx = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]

    # Calculate cumulative variance ratio
    total_variance = np.sum(eigenvalues)
    cumulative_variance = np.cumsum(eigenvalues) / total_variance

    # Find number of components needed to maintain var fraction
    nd = np.argmax(cumulative_variance >= var) + 1

    # Return the top nd eigenvectors as weight matrix
    W = eigenvectors[:, :nd]

    return W
