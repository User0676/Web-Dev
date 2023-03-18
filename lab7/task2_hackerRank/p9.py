# Enter your code here. Read input from STDIN. Print output to STDOUT

x, y = map(int, input().split())
z = int(x / 2 - 0.5)
a = 1
for i in range(z):
    print(''.ljust((z * 3) - (i * 3), '-') + ('.|.' * a) + ''.rjust((z * 3) - (i * 3), '-'))
    a += 2
print('WELCOME'.center(y, '-'))
for i in range(int(x / 2 - 0.5)):
    a -= 2
    print(''.ljust((i + 1) * 3, '-') + ('.|.' * a) + ''.rjust((i + 1) * 3, '-'))