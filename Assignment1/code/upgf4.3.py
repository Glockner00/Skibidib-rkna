import numpy as np
import matplotlib.pyplot as plt
import math

my = (1/2)*2**(-52)
x = np.linspace(-10, 10, 1000)


def value():  # n = 18
    n = 0
    while True:
        if 1/((math.factorial(n))*(np.exp(1))) <= my:
            return n
        n += 1


def min_exp(x, n):
    S = 0.0
    E = 0.0
    Tk = 0
    Tk1 = 0
    if x > 0:
        int_x = math.floor(x)  #integer, down
        fraction_x = x - int_x
        
        for k in range(0, 100):
            Tk = (int_x**k)/math.factorial(k)
            S = S + Tk

        for k in range(0, (n+1)):
            Tk1 = (fraction_x**k)/math.factorial(k)
            E = E + Tk1           
        return (S*E)

    else:
        x = -1 * x
        int_x = math.floor(x)
        fraction_x = x - int_x
        
        for k in range(0, 100):
            Tk = (int_x**k)/math.factorial(k)
            S = S + Tk
        
        for k in range(0, (n+1)):
            Tk1 = (fraction_x**k)/math.factorial(k)
            E = E + Tk1

        return (1/(S*E))

n = value()
min_exp_vals = [min_exp(x_i, n) for x_i in x]
np_exp_vals = [np.exp(x_j) for x_j in x]

relError = [abs(min_exp_vals[k] - np_exp_vals[k])/abs(min_exp_vals[k]) for k in range(len(x))]
plt.plot(x, relError)
plt.show()
