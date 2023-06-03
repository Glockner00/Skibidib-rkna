import numpy as np
import matplotlib.pyplot as plt

#-----DEFINE CONSTANTS------#
n = 100
t = np.linspace(0, 5, n+1)
y = np.zeros(n+1)

#---------------------------#
def E(t):
    for i in range(0, 100):
        if(t[i]>1):
            y[i]=0
        else:
            y[i] = 10000
    return y

#---------------------------#
plt.xlim(0,5)
plt.plot(t, E(t))
plt.title("E(t), uppgift 2.4")
plt.show()
