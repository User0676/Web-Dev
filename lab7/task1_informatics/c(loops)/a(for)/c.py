a = int(input())
b = int(input())

for x in range(b+1):
    if (x**2 >= a) and (x**2<=b):
        print(x**2)

