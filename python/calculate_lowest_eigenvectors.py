"""
This file just makes a simple way to pull out the smallest eigenvalues and their matching eigenvectors from any square
Numpy array. It outputs eigenvalues sorted smallest to largest and a KxM array where row i is the eigenvector
corresponding to eigenvalues[i].
"""

__author__ = "Ashton Switzer"

import numpy as np

def calculate_lowest_eigenvectors(
    square_matrix: np.ndarray,
    number_of_eigenvectors: int = 3
) -> tuple[np.ndarray, np.ndarray]:
    if square_matrix.ndim != 2 or square_matrix.shape[0] != square_matrix.shape[1]:
        raise IndexError(f"Matrix must be square, got {square_matrix.shape}.")
    M = square_matrix.shape[0]
    K = number_of_eigenvectors
    if not (1 <= K <= M):
        raise IndexError(f"K must be between 1 and {M}, got {K}.")

    vals, vecs = np.linalg.eig(square_matrix)
    idx = np.argsort(vals)[:K]               # indices of the K smallest eigenvalues
    eigenvalues = vals[idx]
    eigenvectors = vecs[:, idx].T            # shape (K, M)
    return eigenvalues, eigenvectors


if __name__ == "__main__":
    A = np.array([[2, -1], [-1, 2]], float)
    eigvals, eigvecs = calculate_lowest_eigenvectors(A, 2)

    print("Computed eigenvalues:", eigvals)
    print("Computed eigenvectors:\n", eigvecs)