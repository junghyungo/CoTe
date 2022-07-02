from math import gcd
n = int(input())
ring = list(map(int, input().split()))
for i in range(n-1):
    g = gcd(ring[0], ring[i+1])
    print(f"{ring[0]//g}/{ring[i+1]//g}")