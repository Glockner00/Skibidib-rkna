import numpy as np
import matplotlib.pyplot as plt
 
x = np.linspace(1, 2, 1000)
n = 13 
h = 1/(n-1)

def ApproxArctan(x):
    x_vec = np.linspace(1-h, 2+h, n+2) 
    y_vec = np.arctan(x_vec)

    a = np.searchsorted(x_vec, x) 
    if (a==n):
        a = a-1

    xk = x_vec[a-1:a+3]  
    yk = y_vec[a-1:a+3]  
    f1 = np.polyfit(xk, yk, 3)
    return np.polyval(f1, x)

result = [(abs(ApproxArctan(i)-np.arctan(i))) for i in x]

print(ApproxArctan(i) for i in x)
plt.plot(x, result)
plt.show()

