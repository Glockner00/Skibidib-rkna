n=0
x = 1+(2 ** -n)
while (x != 1):
    print(x)
    n += 1
    x = 1+(2 ** -n)

print("t blir : ", (n-1))
print("My blir : ",(1/2)*2 ** (-(n-1)))