import numpy as np
import matplotlib.pyplot as plt
import math

x1 = np.linspace(-10, 0, 500)
x2 = np.linspace(0, 10, 500)

def min_exp_pos(x2):
    S=0.0
    for k in range(0,100):
        Tk=x2**k/math.factorial(k)
        S=S+Tk
    return S

def min_exp_neg(x1):
    S=0.0
    for k in range(0,100):
        Tk=x1**k/math.factorial(k)
        S=S+Tk
    return 1/S

def f_pos(x2):
    return np.exp(x2)
def f_neg(x1):
    return np.exp(x1)

absError = np.abs(min_exp_neg(x1) - f_neg(x1))
relError = np.abs(absError/f_neg(x1))

absError1 = np.abs(min_exp_pos(x2) - f_pos(x2))
relError1 = np.abs(absError/f_pos(x2))

plt.plot(x1, absError, label='The Absolute Error')
plt.legend()
plt.xlabel('x')
plt.ylabel('Abs_Error')
plt.title('')
plt.show()

plt.plot(x1, relError, label='The Relative Error')
plt.legend()
plt.xlabel('x')
plt.ylabel('Rel_Error')
plt.title('')
plt.show()