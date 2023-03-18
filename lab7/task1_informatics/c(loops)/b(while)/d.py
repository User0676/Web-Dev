n = int(input())

check=True

while n>=2:
    if n%2!=0:
        check=False
        break
    n=n/2

if check:
    print("YES")
else:
    print("NO")
        
    