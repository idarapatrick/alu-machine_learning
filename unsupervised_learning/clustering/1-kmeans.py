#!/usr/bin/env python3
"""Module for performing K-means clustering on a dataset."""
import numpy as np


def kmeans(X, k, iterations=1000):
    """Perform K-means clustering on a dataset.

    Args:
        X: numpy.ndarray of shape (n, d) containing the dataset
        k: positive integer, number of clusters
        iterations: positive integer, maximum number of iterations

    Returns:
        C: numpy.ndarray of shape (k, d) with centroid means for each cluster
        clss: numpy.ndarray of shape (n,) with cluster index for each point
        or None, None on failure
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None, None
    if not isinstance(k, int) or k <= 0:
        return None, None
    if not isinstance(iterations, int) or iterations <= 0:
        return None, None

    n, d = X.shape
    low, high = X.min(axis=0), X.max(axis=0)
    C = np.random.uniform(low, high, size=(k, d))

    for _ in range(iterations):
        dists = np.linalg.norm(X[:, np.newaxis] - C, axis=2)
        clss = np.argmin(dists, axis=1)

        new_C = np.zeros((k, d))
        for i in range(k):
            pts = X[clss == i]
            if len(pts) == 0:
                new_C[i] = np.random.uniform(low, high, size=(d,))
            else:
                new_C[i] = pts.mean(axis=0)

        if np.allclose(C, new_C):
            return new_C, clss
        C = new_C

    dists = np.linalg.norm(X[:, np.newaxis] - C, axis=2)
    clss = np.argmin(dists, axis=1)
    return C, clss
