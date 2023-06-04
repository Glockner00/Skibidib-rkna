import numpy as np
import matplotlib.pyplot as plt

n = 13
x = np.linspace(1, 2, 1000)
h = 1 / (n - 1)

# Interpolationspunkter
xk = np.linspace(1 - h, 2 + h, n + 2)
yk = [np.arctan(x) for x in xk]  # Funktionsvärden vid interpolationspunkterna

# Skriv ut interpolationspunkter och deras funktionsvärden
print("Interpolationspunkter:")
for i in range(len(xk)):
    print("x{} = {:.4f}, y{} = {:.4f}".format(i, xk[i], i, yk[i]))
print()

def ApproxArctan(x):
    a = np.searchsorted(xk, x)
    if (a == n):
        a = a - 1

    xk_interp = xk[a - 1 : a + 3]
    yk_interp = yk[a - 1 : a + 3]
    f1 = np.polyfit(xk_interp, yk_interp, 3)
    return np.polyval(f1, x)

result = np.zeros_like(x)
max_error = 0

for i in range(len(x)):
    error = abs(ApproxArctan(x[i]) - np.arctan(x[i]))
    result[i] = error
    if error > max_error:
        max_error = error

print("Maximalt absolut fel för n = 13:", max_error)

plt.plot(x, result)
plt.xlabel('x')
plt.ylabel('Absolut fel')
plt.title('Absolut fel i approximationen av arctan(x)')
plt.show()

"""
Våra punkter
x0 = 0.9167, y0 = 0.7419
x1 = 1.0000, y1 = 0.7854
x2 = 1.0833, y2 = 0.8254
x3 = 1.1667, y3 = 0.8622
x4 = 1.2500, y4 = 0.8961
x5 = 1.3333, y5 = 0.9273
x6 = 1.4167, y6 = 0.9561
x7 = 1.5000, y7 = 0.9828
x8 = 1.5833, y8 = 1.0075
x9 = 1.6667, y9 = 1.0304
x10 = 1.7500, y10 = 1.0517
x11 = 1.8333, y11 = 1.0714
x12 = 1.9167, y12 = 1.0899
x13 = 2.0000, y13 = 1.1071
x14 = 2.0833, y14 = 1.1233
"""