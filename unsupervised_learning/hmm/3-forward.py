#!/usr/bin/env python3
"""Module to perform the forward algorithm for a hidden markov model."""

import numpy as np


def forward(Observation, Emission, Transition, Initial):
    """Performs the forward algorithm for a hidden markov model."""
    try:
        T = Observation.shape[0]
        N = Emission.shape[0]

        F = np.zeros((N, T))

        # Initialize
        F[:, 0] = Initial[:, 0] * Emission[:, Observation[0]]

        # Recurse
        for t in range(1, T):
            F[:, t] = (np.matmul(F[:, t - 1], Transition) *
                       Emission[:, Observation[t]])

        P = np.sum(F[:, T - 1])
        return P, F
    except Exception:
        return None, None
