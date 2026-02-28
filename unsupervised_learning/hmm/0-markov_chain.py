#!/usr/bin/env python3
"""Module to determine the probability of a markov chain in a
particular state."""

import numpy as np


def markov_chain(P, s, t=1):
    """Determines the probability of a markov chain being in a
    particular state after t iterations."""
    try:
        for _ in range(t):
            s = np.matmul(s, P)
        return s
    except Exception:
        return None
