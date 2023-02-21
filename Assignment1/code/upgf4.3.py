import numpy as np
import matplotlib.pyplot as plt
import math

my = (1/2)*2**(-52)
x = np.linspace(-10, 10, 1000)
e = 2.718281828459045235360287471352662497757


def value():  # n = 18
    n = 0
    while True:
        if 1/((math.factorial(n))*(np.exp(1))) <= my:
            return n
        n += 1


def min_exp(x, n):
    E = 0.0
    Tk1 = 0
    if x > 0:
        int_x = math.floor(x)  #integer, down
        fraction_x = x - int_x

        for k in range(0, (n+1)):
            Tk1 = (fraction_x**k)/math.factorial(k)
            E = E + Tk1           
        
        return (E*(e**int_x))

    else:
        x = -1 * x
        int_x = math.floor(x)
        fraction_x = x - int_x
        
        for k in range(0, (n+1)):
            Tk1 = (fraction_x**k)/math.factorial(k)
            E = E + Tk1

        return (1/(E*(e**int_x)))

n = value()
min_exp_vals = [min_exp(x_i, n) for x_i in x]
np_exp_vals = [np.exp(x_j) for x_j in x]

relError = [abs(min_exp_vals[k] - np_exp_vals[k])/abs(min_exp_vals[k]) for k in range(len(x))]
plt.plot(x, relError)
plt.title("Relative Error")
plt.legend()
plt.show()
