import numpy as np

#-----------DEFINE CONSTANTS-----------#
t = np.linspace(0,1,10)
y = np.linspace(1,1,10) # y_0 = 1.0 

#--------------------------------------#
def funk(t, y ):
    return -y

#------Classic Runge-Kutta mehtod------#
def rk(t):
    for i in range(0, 9):
        h = t[i] - t[i-1]
        k1 = h * funk(t[i], y[i])
        k2 = h * funk(t[i] + (h/2), y[i] + (k1/2))
        k3 = h * funk(t[i] + (h/2), y[i]+ (k2/2))
        k4 = h * funk(t[i] + h, y[i]+k3)
        y[i+1] = y[i] + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
    return y

print(rk(t))

"""
result:
[1.0, 2.70833333, 2.42352352, 2.16866447, 1.94060653, 1.73653129,
 1.55391672, 1.39050599, 1.24427962, 1.1134305 ]
 
"""