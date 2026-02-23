#!/usr/bin/env python3
"""Module for performing the EM algorithm for a GMM."""
import numpy as np
initialize = __import__('4-initialize').initialize
expectation = __import__('6-expectation').expectation
maximization = __import__('7-maximization').maximization


def expectation_maximization(X, k, iterations=1000, tol=1e-5, verbose=False):
    """Perform the expectation maximization algorithm for a GMM.

    Args:
        X: numpy.ndarray of shape (n, d) containing the dataset
        k: positive integer, number of clusters
        iterations: positive integer, maximum number of iterations
        tol: non-negative float, log likelihood tolerance for early stopping
        verbose: boolean, whether to print log likelihood info

    Returns:
        pi, m, S, g, log_l or None, None, None, None, None on failure
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None, None, None, None, None
    if not isinstance(k, int) or k <= 0:
        return None, None, None, None, None
    if not isinstance(iterations, int) or iterations <= 0:
        return None, None, None, None, None
    if not isinstance(tol, float) or tol < 0:
        return None, None, None, None, None
    if not isinstance(verbose, bool):
        return None, None, None, None, None

    pi, m, S = initialize(X, k)
    g, log_l = expectation(X, pi, m, S)

    if verbose:
        print("Log Likelihood after 0 iterations: {}".format(round(log_l, 5)))

    for i in range(1, iterations + 1):
        pi, m, S = maximization(X, g)
        g, log_l_new = expectation(X, pi, m, S)

        if verbose and i % 10 == 0:
            print("Log Likelihood after {} iterations: {}".format(
                i, round(log_l_new, 5)))

        if abs(log_l_new - log_l) <= tol:
            log_l = log_l_new
            if verbose:
                print("Log Likelihood after {} iterations: {}".format(
                    i, round(log_l, 5)))
            break

        log_l = log_l_new

    return pi, m, S, g, log_l
