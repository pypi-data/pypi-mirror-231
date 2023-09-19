"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
import logging
from typing import Tuple

import numpy as np
from scipy.linalg import solve
from scipy.sparse import csr_matrix, identity, spdiags
from scipy.sparse.linalg import spsolve

# logger configuration
logger = logging.getLogger("root")


def fit_line_3d(xyz: np.ndarray) -> np.ndarray:
    """
    Fits a 3D line using least-squares

    Parameters:
    xyz (np.ndarray): A numpy array of shape (n, 3) containing the 3D points

    Returns:
    np.ndarray: A numpy array of shape (3,) containing the direction of the line
    """
    N = np.cov(xyz, rowvar=False)
    return np.linalg.eigh(N)[1][:, -1]


def fit_line_2d(
    x: np.ndarray, y: np.ndarray, weights: np.ndarray = np.array([])
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Fits a 2D line using least-squares

    Parameters:
    x (np.ndarray): A numpy array of shape (n,) containing the x-coordinates of the 2D points
    y (np.ndarray): A numpy array of shape (n,) containing the y-coordinates of the 2D points
    weights (np.ndarray): A numpy array of shape (n,) containing the weights of the points (default is an array of ones)

    Returns:
    Tuple[np.ndarray, np.ndarray, np.ndarray]: A tuple containing the slope, intercept, and residuals of the fitted line
    """
    # design matrix
    A = np.c_[x, np.ones((len(x), 1))]

    if len(weights) == 0:
        weights = np.ones(len(y))

    sigma_ll = spdiags(weights, 0, len(weights), len(weights))

    # solve normal equation
    x_s, l_s, v = least_squares(design_matrix=A, observations=y, sigma_ll=sigma_ll)

    return x_s, l_s, v


def sparse_least_squares(
    design_matrix: csr_matrix, observations: np.ndarray
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Solves a least squares problem with a sparse matrix A and a dense vector l.

    Parameters:
    design_matrix (csr_matrix): A sparse matrix of shape (m, n) representing the design matrix.
    l (np.ndarray): A numpy array of shape (m,) containing the observations.

    Returns:
    Tuple[np.ndarray, np.ndarray, np.ndarray]: A tuple containing the solution vector x_s, the approximated observations l_s, and the residuals v.
    """
    # solve normal equations
    x_s = spsolve(design_matrix.T @ design_matrix, design_matrix.T @ observations)

    # approximated observations
    l_s = design_matrix @ x_s

    # residuals
    v = l_s[:, None] - observations

    return x_s, l_s, v


def least_squares(
    design_matrix: np.ndarray,
    observations: np.ndarray,
    sigma_ll: np.ndarray = np.array([]),
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Solves a least squares problem with a dense matrix A and a dense vector l.

    Parameters:
    design_matrix (np.ndarray): A numpy array of shape (m, n) representing the design matrix.
    observations (np.ndarray): A numpy array of shape (m,) containing the observations.
    sigma_ll (np.ndarray): A numpy array of shape (m, m) containing the weights of the observations (default is an identity matrix).

    Returns:
    Tuple[np.ndarray, np.ndarray, np.ndarray]: A tuple containing the solution vector x_s, the approximated observations l_s, and the residuals v.
    """
    observations = observations.reshape(
        len(observations),
    )
    if sigma_ll.shape[0] == 0:
        sigma_ll = identity(len(observations))
    # solve normal equations
    x_s = solve(
        design_matrix.T @ sigma_ll @ design_matrix,
        design_matrix.T @ sigma_ll @ observations,
    )

    # approximated observations
    l_s = design_matrix @ x_s

    # residuals
    v = l_s - observations

    return x_s, l_s, v


def skew_symmetric_matrix(vector: np.ndarray) -> np.ndarray:
    """
    Returns the skew-symmetric matrix of a 3D vector.

    Parameters:
    vector (np.ndarray): A numpy array of shape (3,) containing the 3D vector.

    Returns:
    np.ndarray: A numpy array of shape (3, 3) containing the skew-symmetric matrix.
    """
    return np.array(
        [
            [0, -vector[2], vector[1]],
            [vector[2], 0, -vector[0]],
            [-vector[1], vector[0], 0],
        ]
    )
