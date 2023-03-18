str = input()

sum = 0

i = 0

for x in str:
    if str[i]=="1":
        sum+= 2**(len(str)-i-1)
    i+=1

print(sum)
