import numpy as np
import matplotlib.pyplot as plt

my = (1/2)*2 ** (-(52))
# orsak för dålig nogranhet är kancellation.
# f(x) = (e^x-1)/x = a/x = b
# |df| <= 3 * my ( enligt felforplanting)

    