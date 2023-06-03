import numpy as np
import matplotlib.pyplot as plt


"""
Uppgift 2.5)
"""
#----DEFINE CONSTANTS------#
T_0 = 291 # 18C -> Kelvin
n = 100
t = np.linspace(0, 5, n+1)
y = np.zeros(len(t))
y_0 = 1

#--------------Classic Runge-Kutta method----------------#
def rk(t, f , y_0):
   
    y[0] = y_0
    h = t[1]-t[0]
    for i in range(0, len(t)-1):
      
        k1 = h * f(t[i], y[i])
        k2 = h * f(t[i] + (h/2), y[i] + (k1/2))
        k3 = h * f(t[i] + (h/2), y[i]+ (k2/2))
        k4 = h * f(t[i] + h, y[i]+k3)
        y[i+1] = y[i] + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
    return y

def GoldTrad(t, T):
    if (t>1):
        E = 0
    else:
        E = 10000
    T = E - 2.76 * 10**(-10) * (T**4-T_0**4)
    return T

f_T = rk(t, GoldTrad, T_0)
plt.title("Uppgift 2.5")
plt.plot(f_T)
plt.show()

"""
Uppgift 2.6)

Detta stämmer då man ser tydligt i grafen att den går
mycket snabbare uppåt i värde än nedåt

"""