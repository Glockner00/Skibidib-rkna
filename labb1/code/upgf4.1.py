import math
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)

def min_exp(x):
    S=0.0
    for k in range(0,100):
        Tk=x**k/math.factorial(k)
        S=S+Tk
    return S

def f(x):
    return np.exp(x)

absError = np.abs(min_exp(x) - f(x))
relError = np.abs(absError/f(x))

plt.plot(x, absError, label='The Absolute Error')
plt.legend()
plt.xlabel('x')
plt.ylabel('Abs_Error')
plt.title('')
plt.show()

plt.plot(x, relError, label='The Relative Error')
plt.legend()
plt.xlabel('x')
plt.ylabel('Rel_Error')
plt.title('')
plt.show()










