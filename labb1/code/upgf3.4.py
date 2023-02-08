import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 16, 161)
x = 10 ** -x

my = (1/2)*2 ** (-(52))

f1 = (np.exp(x)-1)/x
f2 = (x/2)
f3 = (my/np.abs(x))

plt.loglog(x, np.abs(f1-1), label='|f1 - 1|')
plt.loglog(x, (f2+f3), label='R_TOT')
plt.legend()
plt.xlabel('x')
plt.ylabel('Erorr')
plt.title('Beräkningsfelsanalys 3.4')
plt.show()
