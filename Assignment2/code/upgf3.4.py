def div(x,y):
    z = 3/4
    for i in range(1,7):
        z = -y*(z**2)+2*z
    return z*x

print(div(8,1.98))
print(8/1.98)
