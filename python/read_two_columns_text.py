"""
file provides a simple way to read a two-column test file of numbers into a Numpy array of shape (2,M)
The test block reads the data from volumes_energies.dat and prints out the returned array and its shape to confirm
that our result is in that same (2xM) result.
 """

__Author__ = "Ashton Switzer"

import numpy as np

def read_two_columns_text(filename: str) -> np.ndarray:

    # np.loadtxt will raise OSError if the file isn’t found
    arr = np.loadtxt(filename)

    # Handle single-line files: convert 1D to 2D
    if arr.ndim == 1:
        if arr.size != 2:
            raise ValueError(f"Expected two columns in '{filename}', got {arr.size} values.")
        arr = arr[np.newaxis, :]

    # Verify shape is (M, 2)
    if arr.ndim != 2 or arr.shape[1] != 2:
        raise ValueError(f"Expected file '{filename}' to have two columns, got shape {arr.shape}.")

    # Transpose to get shape (2, M)
    return arr.T

if __name__ == "__main__":
    # Test reading the data file
    filename = "volumes_energies.dat"
    data = read_two_columns_text(filename)
    print(f'{data=}, shape={data.shape}')