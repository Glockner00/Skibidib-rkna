from scipy.optimize import fsolve
import numpy as np

def funk(x):
    f = np.sqrt(1+x)*np.exp(x/2) - 2*np.sin(2*x)*(x+x**2)
    return f

x0 =1.35
root, info, _, _ = fsolve(funk, x0, full_output=True)
f_of_root = funk(root)
itterations = info['nfev']

print("Aproximationene av x: ", root[0])
print("Funktionsvärdet: ", f_of_root[0])
print("Antal itterationer: ", itterations)

# Aproximationene av x:  1.3197811068516248
# Funktionsvärdet:  4.440892098500626e-16
# Antal itterationer:  7