#!/usr/bin/env python3
"""Module for calculating a GMM from a dataset using sklearn."""
import sklearn.mixture


def gmm(X, k):
    """Calculate a Gaussian Mixture Model from a dataset.

    Args:
        X: numpy.ndarray of shape (n, d) containing the dataset
        k: number of clusters

    Returns:
        pi: numpy.ndarray of shape (k,) containing the cluster priors
        m: numpy.ndarray of shape (k, d) containing the centroid means
        S: numpy.ndarray of shape (k, d, d) containing covariance matrices
        clss: numpy.ndarray of shape (n,) containing cluster indices
        bic: BIC value for the model
    """
    model = sklearn.mixture.GaussianMixture(n_components=k)
    model.fit(X)
    pi = model.weights_
    m = model.means_
    S = model.covariances_
    clss = model.predict(X)
    bic = model.bic(X)
    return pi, m, S, clss, bic
