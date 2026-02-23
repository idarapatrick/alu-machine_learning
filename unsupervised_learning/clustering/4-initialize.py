#!/usr/bin/env python3
"""Module for initializing Gaussian Mixture Model variables."""
import numpy as np
kmeans = __import__('1-kmeans').kmeans


def initialize(X, k):
    """Initialize variables for a Gaussian Mixture Model.

    Args:
        X: numpy.ndarray of shape (n, d) containing the dataset
        k: positive integer, number of clusters

    Returns:
        pi: numpy.ndarray of shape (k,) with evenly initialized priors
        m: numpy.ndarray of shape (k, d) with centroid means from K-means
        S: numpy.ndarray of shape (k, d, d) with identity covariance matrices
        or None, None, None on failure
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None, None, None
    if not isinstance(k, int) or k <= 0:
        return None, None, None

    n, d = X.shape
    m, _ = kmeans(X, k)
    if m is None:
        return None, None, None

    pi = np.full((k,), 1 / k)
    S = np.tile(np.eye(d), (k, 1, 1))

    return pi, m, S
