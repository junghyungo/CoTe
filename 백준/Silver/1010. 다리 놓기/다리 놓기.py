import sys
input = sys.stdin.readline
import math

for _ in range(int(input())):
    n, m = map(int, input().split())
    
    if (n == m):
        print(1)
        continue
    else:
        print(int(math.factorial(m) / (math.factorial(n) * math.factorial(m-n))))