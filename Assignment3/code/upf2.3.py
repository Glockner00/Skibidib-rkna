from scipy.interpolate import CubicSpline as sc
import numpy as np
import matplotlib.pyplot as plt

n = 5
x = np.linspace(0,1,n)

def f(x):
    return (4/3)*(x**4) - (4/3)*(x**3) + (1/2)*(x**2)

y = f(x)
x_plot = np.linspace(0,1,100)

f_derivate_0 = 0
f_derivate_1 = 7/3
cs = sc(x, y, bc_type=((1, f_derivate_0), (1, f_derivate_1)))

plt.figure()
plt.plot(x_plot, f(x_plot), label='f(x)')
plt.plot(x_plot, cs(x_plot), label='sh(x)')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('f(x) and sh(x)')

plt.figure()
plt.plot(x_plot, np.abs(f(x_plot)- cs(x_plot)))
plt.xlabel('x')
plt.ylabel('Absolut error')
plt.title('|f(x) - sh(x)|')
plt.show()



