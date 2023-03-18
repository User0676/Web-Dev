x = [i for i in str(input())]
d = int(input())
k = 0
for i in x:
   if str(d) == i:
       k += 1
print(k)