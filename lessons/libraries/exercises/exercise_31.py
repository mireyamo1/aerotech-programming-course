import numpy as np
import time
from scipy.integrate import quad

def f(x):
    return np.sin(x)

a, b = 0, np.pi / 2
n = 1000
dx = (b-a) / n
x_vals = np.linspace(a, b, n)

# Riemann way
t0_riemann = time.perf_counter()
riemann_integral = np.sum(f(x_vals) * dx)
tf_riemann = time.perf_counter()
riemann_time = tf_riemann - t0_riemann

# Direct way
t0_scipy = time.perf_counter()
scipy_integral, _ = quad(f, a, b)
tf_scipy = time.perf_counter()
scipy_time = tf_scipy - t0_scipy

print("Riemann Sum with", n, "intervals:", riemann_integral)
print("SciPy Integration:", scipy_integral)

time_difference = riemann_time - scipy_time

print("Difference between Riemann and Scipy is: ", time_difference)