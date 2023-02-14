import matplotlib.pyplot as plt
import numpy as np
import math

x_values = np.linspace(0, 1, 1000)
my = (1/2)*2**(-52)


def min_exp(x, n):
    t = 1
    result = 1
    # t_(k) = t_(k-1) * (x/k)
    for k in range(1, n):
        t *= (x/k)
        result += t
    return result


def n():  # n = 18
    n = 0
    while True:
        if (1**n)/((math.factorial(n))*(np.exp(1))) <= my:
            return n
        n += 1


n = n()
e_taylor = [min_exp(x_i, n) for x_i in x_values]
np_exp_vals = [np.exp(x_j) for x_j in x_values]

plt.title("Number of terms in taylor-series")
plt.plot(x_values, e_taylor, label="Calculated with n={}".format(n))
plt.plot(x_values, np_exp_vals, label="Numpy")
plt.legend()
plt.show()

plt.title("Relative Error")
relError = [abs(e_taylor[k] - np_exp_vals[k]) for k in range(len(x_values))]
plt.plot(x_values, relError, label="|taylor_exp(x) - numpy_exp(x)|")
plt.legend()
plt.show()
