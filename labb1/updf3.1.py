import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 16, 161)
x = 10 ** -x
f1 = (np.exp(x)-1)/x

max_index = np.argmax(np.abs(f1-1))
min_index = np.argmin(np.abs(f1-1))

plt.loglog(x,np.abs(f1-1))
plt.plot(x[max_index], np.abs(f1-1)[max_index], 'ro', markersize=10)
plt.plot(x[min_index], np.abs(f1-1)[min_index], 'bo', markersize=10)
plt.show()
print("Det största värdet blir :" , max_index)
print("Det minsta värdet blir :" , min_index)

#Vid små x så ökar felet. Det minsta felet fås när x ungefär är 1,48 * 10^-8

