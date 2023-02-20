import matplotlib.pyplot as plt
import numpy as np
import math

x_values = np.linspace(-10, 10, 1000)
my = (1/2)*2**(-52)


def min_exp(x):
    n = 18
    t = 1
    
    result = 0
    # t_(k) = t_(k-1) * (x/k)

    if x>0:
        for k in range(1, n):
            t *= (x/k)
            result += t
        return result
    
    else:
        for k in range(1, n):
            x = -1 * x
            t *= (x/k)
            result += t
    return (1/result)

def n():  # n = 18
    n = 0
    while True:
        if (1**n)/((math.factorial(n))*(np.exp(1))) <= my:
            return n
        n += 1


e_taylor = [min_exp(x_i) for x_i in x_values]
np_exp_vals = [np.exp(x_j) for x_j in x_values]

plt.title("Number of terms in taylor-series")
plt.plot(x_values, e_taylor, label="Calculated with n={}".format(n()))
plt.plot(x_values, np_exp_vals, label="Numpy")
plt.legend()
plt.show()

plt.title("Relative Error")
relError = [abs(e_taylor[k] - np_exp_vals[k])/abs(e_taylor[k]) for k in range(len(x_values))]
plt.plot(x_values, relError)
plt.legend()
plt.show()
