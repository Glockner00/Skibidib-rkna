"""
sqrt(2) = 1.4142135623730951 
signifikanta siffror = (på exakta värdet eller det absoluta felet ? )
delta a = närmevärdet(a) - exakta värdet(a) // absoluta felet
"""
import math
my = (1/2)*2 ** (-(52))
abs_err = (my/math.sqrt(2))
print(abs_err)

# 16 signifikanta decimaler och datorns approximation har 16 korrekta decimaler.
# den övre gränsen av det absoluta felet är 7.85 * 10^-17  