a = input().split()

maxEl = int(a[0])
maxPos = 0

for i in range(0,len(a)):
    if int(a[i])>maxEl:
        maxEl = int(a[i])
        maxPos = i
    
print(maxEl,maxPos)
