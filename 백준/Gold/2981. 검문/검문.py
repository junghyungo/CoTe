from math import gcd

a = []
for i in range(int(input())):
    a.append(int(input()))
a.sort()

b = []
for i in range(len(a)-1):
    b.append(a[i+1]-a[i])
b.sort()

n = b[0]
for i in range(1, len(b)):
    n = gcd(n, b[i])

c = set()
for i in range(2, int(n**0.5)+1):
    if n%i == 0:
        c.add(i)
        c.add(n//i)
c.add(n)
print(*sorted(list(c)))