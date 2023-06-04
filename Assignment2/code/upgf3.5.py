import matplotlib.pyplot as plt
import numpy as np
y = np.linspace(1,2,1000)

def div(x,y):
    z = 3/4
    for i in range(1,7):
        z = -y*(z**2)+2*z
    return z*x

print(div(8,1.98))
print(8/1.98)

plt.plot(y, np.abs(div(1.32, y) - 1.32/y))
plt.show()
