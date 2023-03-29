import numpy as np
import matplotlib.pyplot as plt

y = np.linspace(1,2,1000)
y_k = np.linspace(1,2,8)
z_k = 1/y_k # list of all z_k values

def div(x,y,z):
    for i in range(1,6):
        z = -y*(z**2)+2*z
    return z*x

for i in range(len(y_k)-1):
    y_subtraction = y[(y>= y_k[i]) & (y < y_k[i+1])]
    plt.plot(y_subtraction, abs(div(1.32, y_subtraction, z_k[i]) - 1.32/y_subtraction ))

plt.show()

