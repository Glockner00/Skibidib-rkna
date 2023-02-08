import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 16, 161)
x = 10 ** -x

my = (1/2)*2 ** (-(52))

f2 = (np.exp(x)-1)/ (np.log(np.exp(x)))
f3 = (x/2)
f4 = (my/2)

plt.loglog(x, np.abs(f2-1), label='|f2 - 1|')
plt.loglog(x, (f3+f4), label='R_TOT')
plt.legend()
plt.xlabel('x')
plt.ylabel('Erorr')
plt.title('Beräkningsfelanalys 3.5')
plt.show()
