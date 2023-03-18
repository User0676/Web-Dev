a = int(input())

i=2

while i<=a/2:
    if a%i==0:
        print(i)
        break
    i+=1
else:
    print(a)