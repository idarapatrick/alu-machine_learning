#!/usr/bin/env python3
"""Module for finding the best number of clusters for a GMM using BIC."""
import numpy as np
expectation_maximization = __import__('8-EM').expectation_maximization


def BIC(X, kmin=1, kmax=None, iterations=1000, tol=1e-5, verbose=False):
    """Find the best number of clusters for a GMM using the BIC.

    Args:
        X: numpy.ndarray of shape (n, d) containing the dataset
        kmin: positive integer, minimum number of clusters (inclusive)
        kmax: positive integer, maximum number of clusters (inclusive)
        iterations: positive integer, maximum iterations for EM
        tol: non-negative float, tolerance for EM
        verbose: boolean, whether EM should print info

    Returns:
        best_k: best value for k based on BIC
        best_result: tuple of (pi, m, S) for the best k
        l: numpy.ndarray of shape (kmax - kmin + 1) with log likelihoods
        b: numpy.ndarray of shape (kmax - kmin + 1) with BIC values
        or None, None, None, None on failure
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None, None, None, None
    if not isinstance(kmin, int) or kmin <= 0:
        return None, None, None, None
    if kmax is None:
        kmax = X.shape[0]
    if not isinstance(kmax, int) or kmax <= 0:
        return None, None, None, None
    if kmax - kmin < 1:
        return None, None, None, None
    if not isinstance(iterations, int) or iterations <= 0:
        return None, None, None, None
    if not isinstance(tol, float) or tol < 0:
        return None, None, None, None
    if not isinstance(verbose, bool):
        return None, None, None, None

    n, d = X.shape
    results = []
    likelihoods = []
    bics = []

    for k in range(kmin, kmax + 1):
        pi, m, S, g, lk = expectation_maximization(
            X, k, iterations, tol, verbose)
        if pi is None:
            return None, None, None, None

        results.append((pi, m, S))
        likelihoods.append(lk)

        # p = k-1 priors + k*d means + k*d*(d+1)/2 covariance params
        p = k - 1 + k * d + k * d * (d + 1) // 2
        bics.append(p * np.log(n) - 2 * lk)

    l = np.array(likelihoods)
    b = np.array(bics)

    best_idx = np.argmin(b)
    best_k = kmin + best_idx
    best_result = results[best_idx]

    return best_k, best_result, l, b
