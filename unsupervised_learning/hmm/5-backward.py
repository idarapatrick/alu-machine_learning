#!/usr/bin/env python3
"""Module to perform the backward algorithm for a hidden markov model."""

import numpy as np


def backward(Observation, Emission, Transition, Initial):
    """Performs the backward algorithm for a hidden markov model."""
    try:
        T = Observation.shape[0]
        N = Emission.shape[0]

        B = np.zeros((N, T))

        # Initialize
        B[:, T - 1] = 1

        # Recurse backwards
        for t in range(T - 2, -1, -1):
            B[:, t] = np.matmul(
                Transition,
                Emission[:, Observation[t + 1]] * B[:, t + 1]
            )

        P = np.sum(Initial[:, 0] * Emission[:, Observation[0]] * B[:, 0])
        return P, B
    except Exception:
        return None, None
