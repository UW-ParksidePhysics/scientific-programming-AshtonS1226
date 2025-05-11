import matplotlib.pyplot as plt


def parse_sum_output(filename):
    """Parse logarithmic_sum.out file and return tolerances, errors, and maximum indices."""
    tolerances = []
    errors = []
    max_indices = []

    with open(filename, 'r') as file:
        for line in file:
            if line.startswith("epsilon:"):
                parts = line.replace(',', '').split()
                epsilon = float(parts[1])
                error = float(parts[4])
                n = int(parts[6].split('=')[-1])
                tolerances.append(epsilon)
                errors.append(error)
                max_indices.append(n)

    return tolerances, errors, max_indices


def plot_logarithmic_sum_error(tolerances, errors, max_indices):
    """Plot approximation error versus n using a log scale on the y-axis."""
    plt.figure()
    plt.semilogy(max_indices, errors, marker='o', linestyle='-', color='blue')
    plt.xlabel('Maximum Index (n)')
    plt.ylabel('Approximation Error (Δ)')
    plt.title('Logarithmic Sum Error vs n')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    filename = 'logarithmic_sum.out'
    tolerances, errors, max_indices = parse_sum_output(filename)
    plot_logarithmic_sum_error(tolerances, errors, max_indices)
