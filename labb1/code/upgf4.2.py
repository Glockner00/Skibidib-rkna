import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-10, 10, 1000)


def min_exp(x):
    S = 0.0
    arr = x
    for i in arr:
        if i > 0:
            for k in range(0, 100):
                Tk = i**k/math.factorial(k)
                S = S+Tk
            return S
        else:
            i = -1 * i
            for k in range(0, 100):
                Tk = i**k/math.factorial(k)
                S = S+Tk
            return 1/S


absError = np.abs(min_exp(x) - np.exp(x))
relError = np.abs(absError/np.exp(x))

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
