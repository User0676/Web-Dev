a = input().split()

memory = int(a[0])

for i in range(1,len(a)):
    if int(a[i])>memory:
        print(a[i],end=' ')
    memory = int(a[i])