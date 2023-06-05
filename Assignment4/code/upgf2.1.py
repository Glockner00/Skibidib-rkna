import numpy as np

#-----------DEFINE CONSTANTS-----------#
t = np.linspace(0, 1, 10)
y = np.linspace(0, 1, 10)
y0 = 1 

#--------------------------------------#
def funk(t, y):
    return -y

#------Classic Runge-Kutta method------#
def rk(t, f, y0):
    y[0] = y0
    for i in range(1, len(t)):
        h = t[1] - t[0]
        k1 = h * f(t[i-1], y[i-1])
        k2 = h * f(t[i-1] + (h/2), y[i-1] + (k1/2))
        k3 = h * f(t[i-1] + (h/2), y[i-1] + (k2/2))
        k4 = h * f(t[i-1] + h, y[i-1] + k3)
        y[i] = y[i-1] + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
    return y

result = rk(t, funk, y0)
y_1 = result[-1]  # y(1) vid t = 1

print(f"y(1) ≈ {y_1}")