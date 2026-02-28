#!/usr/bin/env python3
"""Module to determine the steady state probabilities of a regular markov chain."""

import numpy as np


def regular(P):
    """Determines the steady state probabilities of a regular markov chain."""
    try:
        if P.ndim != 2 or P.shape[0] != P.shape[1]:
            return None
        if not np.allclose(P.sum(axis=1), 1):
            return None

        # Check if regular: some power of P has all positive entries
        n = P.shape[0]
        power = P.copy()
        for _ in range(100):
            if np.all(power > 0):
                break
            power = np.matmul(power, P)
        else:
            return None

        # Iterate to find steady state
        s = np.ones((1, n)) / n
        for _ in range(10000):
            s_new = np.matmul(s, P)
            if np.allclose(s_new, s):
                return s_new
            s = s_new
        return None
    except Exception:
        return None
