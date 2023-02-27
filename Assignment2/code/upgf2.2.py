import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import numpy as np

x = np.linspace(0, 3, 1000)

def funk(x):
    f = np.sqrt(1+x)*np.exp(x/2)-2*np.sin(2*x)*(x+x**2)
    return f

max_iterations = 100 
tolerance = 0.5*2**(-52) # Toleranse för konvergens

root = 1.35  # första gissnig
iterations = 0  

while iterations < max_iterations:
    iterations += 1
    prev_root = root
    print("prev rot",prev_root)
    root = fsolve(funk, prev_root)
    print("rot ",root)

    print("abs: ", abs(root-prev_root))
    if abs(root - prev_root) < tolerance:
        break

print(f"Rot:", root[0])
print(f"Antal itterationer: ", iterations)
print(f"Funktionsvärde:", funk(root[0]))