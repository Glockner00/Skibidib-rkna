import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as pp
import math


def ApproxArctan(x):
    n = 100 #interpolationspunkter
    h = 1/(n-1) 
    x_vec = np.linspace(1-h, 2+h, n+2) # skapar interpolationspunkter som en vektor.
    y_vec = np.arctan(x_vec) # y vektorn
    a = np.searchsorted(x_vec, x) -1 
    k = (y_vec[a+1] - y_vec[a]) / (x_vec[a+1] - y_vec[a]) 
    m = y_vec[a] - k*x_vec[a] 
    Approx = k*x + m
    return Approx

print("Approx: ",ApproxArctan(1.49))
print("Numpy approx: ",np.arctan(1.49))

"""
utskrift.
0.9781301906312261 - vår approximation.
0.9797025429849916 - numpys aproximation.

"""