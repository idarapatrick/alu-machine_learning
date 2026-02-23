#!/usr/bin/env python3
"""Module for performing PCA on a dataset."""
import numpy as np


def pca(X, var=0.95):
    """Perform PCA on a dataset to maintain a fraction of variance.

    Args:
        X: numpy.ndarray of shape (n, d) with zero mean across all dimensions
        var: fraction of variance the PCA transformation should maintain

    Returns:
        W: numpy.ndarray of shape (d, nd) containing the weights matrix
    """
    u, s, Vt = np.linalg.svd(X)
    cumvar = np.cumsum(s ** 2) / np.sum(s ** 2)
    nd = np.argmax(cumvar >= var) + 1
    return Vt[:nd].T
