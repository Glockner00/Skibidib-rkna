n=0
n_counter = 0
x = 1+(2 ** -n)
while (x != 1):
    print(x)
    n_counter +=1
    n += 1
    x = 1+(2 ** -n)

print("t blir : ", n)
print("My blir : ",(1/2)*2 ** (-n))