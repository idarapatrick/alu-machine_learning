#!/usr/bin/env python3
"""Module to perform the Baum-Welch algorithm for a hidden markov model."""

import numpy as np


def baum_welch(Observations, Transition, Emission, Initial, iterations=1000):
    """Performs the Baum-Welch algorithm for a hidden markov model."""
    try:
        T = Observations.shape[0]
        M = Transition.shape[0]
        N = Emission.shape[1]

        for _ in range(iterations):
            # Forward pass
            F = np.zeros((M, T))
            F[:, 0] = Initial[:, 0] * Emission[:, Observations[0]]
            for t in range(1, T):
                F[:, t] = np.matmul(F[:, t - 1], Transition) * Emission[:, Observations[t]]

            # Backward pass
            B = np.zeros((M, T))
            B[:, T - 1] = 1
            for t in range(T - 2, -1, -1):
                B[:, t] = np.matmul(
                    Transition,
                    Emission[:, Observations[t + 1]] * B[:, t + 1]
                )

            # Compute xi and gamma
            xi = np.zeros((M, M, T - 1))
            for t in range(T - 1):
                denom = np.matmul(
                    np.matmul(F[:, t], Transition) * Emission[:, Observations[t + 1]],
                    B[:, t + 1]
                )
                for i in range(M):
                    xi[i, :, t] = (F[i, t] * Transition[i, :] *
                                   Emission[:, Observations[t + 1]] *
                                   B[:, t + 1]) / denom

            gamma = np.sum(xi, axis=1)
            # Add last time step to gamma
            gamma_full = np.hstack([gamma, np.sum(xi[:, :, T - 2], axis=1).reshape(-1, 1)])

            # Update Transition
            Transition = np.sum(xi, axis=2) / np.sum(gamma, axis=1).reshape(-1, 1)

            # Update Emission
            denom = np.sum(gamma_full, axis=1)
            for k in range(N):
                Emission[:, k] = np.sum(gamma_full[:, Observations == k], axis=1) / denom

        return Transition, Emission
    except Exception:
        return None, None
