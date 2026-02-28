#!/usr/bin/env python3
"""Module to determine if a markov chain is absorbing."""

import numpy as np


def absorbing(P):
    """Determines if a markov chain is absorbing."""
    try:
        if P.ndim != 2 or P.shape[0] != P.shape[1]:
            return False
        if not np.allclose(P.sum(axis=1), 1):
            return False

        n = P.shape[0]

        # Find absorbing states (diagonal = 1)
        absorbing_states = set(np.where(np.diag(P) == 1)[0])

        if not absorbing_states:
            return False

        # Check if every state can reach an absorbing state
        # Use reachability: expand set of states that can reach
        # absorbing states
        reachable = absorbing_states.copy()
        changed = True
        while changed:
            changed = False
            for i in range(n):
                if i not in reachable:
                    for j in reachable:
                        if P[i, j] > 0:
                            reachable.add(i)
                            changed = True
                            break

        return len(reachable) == n
    except Exception:
        return False
