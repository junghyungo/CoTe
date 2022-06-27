n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
c = a&set(b)
for i in range(m):
    if b[i] in c: print(1)
    else: print(0)