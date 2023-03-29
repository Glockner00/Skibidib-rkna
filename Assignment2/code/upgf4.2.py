import numpy as np
import matplotlib.pyplot as plt

n = 100
x = np.linspace(1-1/(n-1), 2+1/(n-1), n+2)

def ApproxArctan(x):
    y = np.arctan(x)
    return y

def y_vals():
    vals = []
    for k in xValues:
        vals.append(ApproxArctan(k))
    return vals

def x_vals():
    vals = []
    for k in range(0, n+1):
        x_k = 1 + (k-1)/(n-1)
        vals.append(x_k)
    return vals

xValues = x_vals()
yValues = y_vals()

p1 = np.polyfit(xValues, yValues, deg=1)
p1_vals = np.polyval(p1, x)

plt.plot(xValues, yValues)
plt.plot(x,p1_vals)
plt.show()
