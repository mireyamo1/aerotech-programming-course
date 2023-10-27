import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2*np.pi, 0.1)
y = (np.sin(x))

plt.grid(True)
plt.title("sin(x) function ")

plt.plot(x, y)
plt.show()
