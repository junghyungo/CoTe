import sys
input = sys.stdin.readline

n,m = map(int,input().split())
pkm = {}
num = {}

for i in range(n):
    a = input().rstrip()
    pkm[a] = i+1
    num[i+1] = a

for i in range(m):
    a = input().rstrip()
    if a.isdigit(): print(num[int(a)])
    else: print(pkm[a])