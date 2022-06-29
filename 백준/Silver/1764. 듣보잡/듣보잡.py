import sys
imput = sys.stdin.readline

n,m = map(int, input().split())

list_n = []
for i in range(n):
  list_n.append(input())

list_m = []
for i in range(m):
  list_m.append(input())

a = set(list_n)&set(list_m)
a = list(a)
a.sort()
print(len(a))
for i in a: print(i)