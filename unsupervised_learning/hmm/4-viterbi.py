#!/usr/bin/env python3
"""Module to calculate the most likely sequence of hidden states for a hidden markov model."""

import numpy as np


def viterbi(Observation, Emission, Transition, Initial):
    """Calculates the most likely sequence of hidden states for a hidden markov model."""
    try:
        T = Observation.shape[0]
        N = Emission.shape[0]

        V = np.zeros((N, T))
        backpointer = np.zeros((N, T), dtype=int)

        # Initialize
        V[:, 0] = Initial[:, 0] * Emission[:, Observation[0]]

        # Recurse
        for t in range(1, T):
            trans_prob = V[:, t - 1].reshape(-1, 1) * Transition
            backpointer[:, t] = np.argmax(trans_prob, axis=0)
            V[:, t] = np.max(trans_prob, axis=0) * Emission[:, Observation[t]]

        # Backtrack
        path = [np.argmax(V[:, T - 1])]
        for t in range(T - 1, 0, -1):
            path.append(backpointer[path[-1], t])
        path.reverse()

        P = np.max(V[:, T - 1])
        return path, P
    except Exception:
        return None, None
