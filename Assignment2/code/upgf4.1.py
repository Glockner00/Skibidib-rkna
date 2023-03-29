import numpy as np 
import matplotlib.pyplot as plt

x = [0.9, 1.1, 1.2]
f = [0.4710, 0.2452, 0.2385]
p2 = np.polyfit(x,f,3)

n = 100
xx = np.linspace(0.9,1.2,n)
pvals = np.polyval(p2, xx)
plt.plot(x,f, 'x')
plt.plot(xx, pvals)
plt.show()

