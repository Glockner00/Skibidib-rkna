import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-10, 10, 1000)


def min_exp(x):
    S = 0.0
    if x > 0:
        for k in range(0, 100):
            Tk = x**k/math.factorial(k)
            S = S + Tk
        return S
    else:
        x = -1 * x
        for k in range(0, 100):
            Tk = x**k/math.factorial(k)
            S = S + Tk
        return 1/S


min_exp_vals = [min_exp(x_i) for x_i in x]
np_exp_vals = [np.exp(x_j) for x_j in x]
relError = [abs(min_exp_vals[k] - np_exp_vals[k]) for k in range(len(x))]
plt.plot(x, relError)
plt.show()
"""
Annledningn till att vi använder exp(-x) = 1/exp(x) är :
    för x < 0 blir serien:
        exp(-x) = -f1 + f2 - f3 + f4 - ...

    De negativa termerna(som är väldigt små) "balanserar" ut de positiva termer 
    (som är väldigt stora). Men eftersom att serien är finit kommer det att boli en ojämn balans.
    Det kommer bli en term som inte balansers, vilket leder till ett stort fel. Detta problem finns
    inte för för exp(x) då x>0, och vi får alltså en snabbare komvergens genom att använda 
    exp(-x) = 1 / exp(x).
"""
