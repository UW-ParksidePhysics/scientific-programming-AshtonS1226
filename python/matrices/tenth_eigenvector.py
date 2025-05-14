import numpy as np
import matplotlib.pyplot as plt

matrix_dimension = 10
h = 1 / (matrix_dimension + 1)

main_diag = 2 * np.ones(matrix_dimension)
off_diag = -1 * np.ones(matrix_dimension - 1)
H = (1 / (2 * h**2)) * (np.diag(main_diag) + np.diag(off_diag, k=1) + np.diag(off_diag, k=-1))

eigenvalues, eigenvectors = np.linalg.eig(H)

idx = np.argsort(eigenvalues)
eigenvectors = eigenvectors[:, idx]

tenth_vector = eigenvectors[:, 9]

x_values = np.linspace(1 / (matrix_dimension + 1), matrix_dimension / (matrix_dimension + 1), matrix_dimension)
analytic = np.sqrt(2) * np.sin(np.pi * x_values)

plt.figure(figsize=(8, 5))
plt.plot(x_values, tenth_vector, 'o-', label='10th Eigenvector')
plt.plot(x_values, analytic, '--', label=r'$\sqrt{2} \sin(\pi x)$')
plt.title("10th Eigenvector vs Analytical Function")
plt.xlabel("x")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
