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
    # Perform SVD on the data matrix
    # For mean-centered data: X = U * S * V^T
    # The columns of V are the principal components (eigenvectors of X^T X)
    # The singular values S relate to eigenvalues: eigenvalue = (S^2) / n
    U, S, Vt = np.linalg.svd(X, full_matrices=False)
    
    # V^T rows are the principal components, we need V columns
    eigenvectors = Vt.T
    
    # Calculate eigenvalues from singular values
    eigenvalues = (S ** 2) / X.shape[0]

    # Calculate cumulative variance ratio
    total_variance = np.sum(eigenvalues)
    cumulative_variance = np.cumsum(eigenvalues) / total_variance

    # Find number of components needed to maintain var fraction
    nd = np.argmax(cumulative_variance >= var) + 1

    # Return the top nd eigenvectors as weight matrix
    # Ensure real values (SVD might return complex for numerical reasons)
    W = eigenvectors[:, :nd].real

    return W
