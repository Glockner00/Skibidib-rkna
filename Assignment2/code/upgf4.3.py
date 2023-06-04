import numpy as np
import matplotlib.pyplot as plt

def ApproxArctan(x):
    n = 5
    h = 1/(n-1)

    x_vec = np.linspace(1-h, 2+h, n+2)
    y_vec = np.arctan(x_vec)

    a = np.searchsorted(x_vec, x) - 1

    k = (y_vec[a+1] - y_vec[a]) / (x_vec[a+1] - y_vec[a])
    m = y_vec[a] - k * x_vec[a]

    Approx = k*x + m
    return Approx

x = np.linspace(1, 2, 1000)
abs_err = np.abs(ApproxArctan(x)-np.arctan(x))
print(ApproxArctan(1.49))
print(np.arctan(1.49))

plt.plot(x, abs_err)
plt.show()