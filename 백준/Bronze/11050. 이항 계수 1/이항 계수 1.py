n,k = map(int, input().split())
a = 1
b = 1
for i in range(k):
    a *= n
    n -= 1
    b *= k
    k -= 1
print(a//b)