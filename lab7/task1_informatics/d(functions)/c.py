def XOR(a,b):
    if a!=b:
        return 1
    else:
        return 0
    
arr = input().split()

a = arr[0]
b = arr[1]

print(XOR(a,b))