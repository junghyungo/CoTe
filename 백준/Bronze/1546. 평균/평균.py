n = int(input())
a = list(map(int, input().split()))
b = []
m = max(a)
for i in a: b.append(i/m*100)
print(sum(b)/n)