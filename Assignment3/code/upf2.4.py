import numpy as np
from scipy.interpolate import CubicSpline

# Definiera funktionen f(x)
def f(x):
    return (4/3)*x**4 - (4/3)*x**3 + (1/2)*x**2

# Beräkna derivatorna i ändpunkterna
f_derivative_0 = 0
f_derivative_1 = 7/3

# Lista med antal interpolationspunkter
n_values = [11, 21, 41]

# Beräkna maximala felet för varje n
max_errors = []

for n in n_values:
    x = np.linspace(0, 1, n)
    y = f(x)

    # Använd kubisk spline-interpolering med rätta ändpunktsvillkor
    cs = CubicSpline(x, y, bc_type=((1, f_derivative_0), (1, f_derivative_1)))

    # Skapa x-värden för plottning
    x_plot = np.linspace(0, 1, 1000)

    # Beräkna det maximala felet
    max_error = np.max(np.abs(f(x_plot) - cs(x_plot)))
    max_errors.append(max_error)

    print(f'n = {n}, Maximalt fel: {max_error}')

# Beräkna |RT(h)| för h = 1/10, h = 1/20 och h = 1/40
h_values = [1/10, 1/20, 1/40]
RT_values = [max_errors[0] * (1/10)**p for p in range(1, 4)]

for h, RT in zip(h_values, RT_values):
    print(f'|RT({h})| = {RT}')