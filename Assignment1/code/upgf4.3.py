import numpy as np
import matplotlib.pyplot as plt
import math

my = (1/2)*2**(-52)
x_values = np.linspace(-10, 10, 1000)

def n():  # n = 18
    n = 0
    while True:
        if (1**n)/((math.factorial(n))*(np.exp(1))) <= my:
            return n
        n += 1

def new_min_exp(x):
    Tk1 = 0
    Tk = 0
    S = 0  # integer
    E = 0  # fraction   

    if x > 0:
        int_x = int(x) # Avrudnar nedåt
        fraction = x - int_x

        for k in range(100):
            Tk = (int_x ** k) / math.factorial(k) 
            S = S + Tk

        for k in range(18):
            Tk1 = x**k/math.factorial(k)
            E = E + Tk1

        return (S * E) 

    else:
        x = -1 * x
        int_x = int(x) # Avrudnar nedåt
        fraction = x - int_x
        for k in range(100):
            Tk = (int_x**k)/math.factorial(k)
            S = S + Tk

        for k in range(18):
            Tk1 = (fraction ** k)/math.factorial(k)
            E = E + Tk1
        
        return (1/(S*E))

    
e_taylor = [new_min_exp(x_i) for x_i in x_values]
np_exp_vals = [np.exp(x_j) for x_j in x_values]

plt.title("Number of terms in taylor-series")
plt.plot(x_values, e_taylor, label="Calculated with n={}".format(n()))
plt.plot(x_values, np_exp_vals, label="Numpy")
plt.legend()
plt.show()

relError = [abs(e_taylor[k] - np_exp_vals[k])/abs(e_taylor[k]) for k in range(len(x_values))]
plt.plot(x_values, relError)
plt.title("Relative Error")
plt.show()
