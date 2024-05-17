import numpy as np
from matplotlib import pyplot as plt

def func_py(x: list[float], N: int) -> list[float]:
    """
    Calculate function values for passed array of arguments
    """
    return [1 - ((t - N/2) / (N/2)) ** 2 for t in x]

def tabulate_py(a: float, b: float, n: int, N: int) -> dict[float]:
    x = [a + x * (b - a) / n for x in range(n)]
    y = func_py(x, N)
    return x, y

def tabulate_np(a: float, b: float, n: int, N: int) -> np.ndarray:
    x = np.linspace(a, b, n)
    y = 1 - ((x - N/2) / (N/2)) ** 2
    return x, y

def test_tabulation(f, a, b, n, N, axis):
    res = f(a, b, n, N)
    axis.plot(res[0], res[1])
    axis.grid()

def main():
    a, b, n, N = 0, 1, 1000, 11

    fig, (ax1, ax2) = plt.subplots(2, 1)
    res = test_tabulation(tabulate_py, a, b, n, N, ax1)
    res = test_tabulation(tabulate_np, a, b, n, N, ax2)
    plt.show()

if __name__ == '__main__':
    main()
