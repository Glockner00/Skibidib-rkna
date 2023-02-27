from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import numpy as np

def funk(x):
    f = np.sqrt(1+x)*np.exp(x/2) - 2*np.sin(2*x)*(x+x**2)
    return f

def evaluations(x):
    values = funk(x)
    if np.shape(values) != (1,):
        values = np.array([values])
    evaluations.fevals.append(values)
    return values[0]

evaluations.fevals = []

result = fsolve(evaluations, 1.35)

print("Rot: ", result)
print("Funktionsvärden vid varje itteration: ", evaluations.fevals)

fevals = np.array(evaluations.fevals).flatten()
x_vals = np.arange(len(fevals))

plt.plot(x_vals, fevals)
plt.xlabel("Iteration")
plt.ylabel("f(x)")
plt.title("Funktionsvärden vid varje itteration av fsolve")
plt.show()