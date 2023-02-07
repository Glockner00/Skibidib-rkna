import numpy as np
import matplotlib.pyplot as plt 

x = np.linspace(-2 -2, 100)
n = 5 # number of terms in the Taylor series, max number of terms we could approximate. 

def f(x):
    return (np.exp(x)-1)/x

def exp_taylor(x, n):
    result = 0
    for i in range(n):
        result += x**i/np.math.factorial(i)
    return result

y_true = f(x)

y_taylor = exp_taylor(x, n)  # Approximation using the Taylor series

RT = np.abs(y_true-y_taylor)
print(RT)
plt.plot(x, RT, label='RT')
plt.legend()
plt.xlabel('x')
plt.ylabel('RT')
plt.title(f'Truncation Error RT with {n} terms in Tylor series')
plt.show()

# Vi har plottat y = e^x - 1 / x med hjälp av en taylor serie och jämfört med tidigare uppgift. 
# trunkeringsfelet (approximiationen - exakt värde)  = 8.41877679e-11 ? 