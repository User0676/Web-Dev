def minNum(a,b,c,d):
    return min(min(a,b),min(c,d))

arr = input().split()

a = int(arr[0])
b = int(arr[1])
c = int(arr[2])
d = int(arr[3])




print(minNum(a,b,c,d))

            