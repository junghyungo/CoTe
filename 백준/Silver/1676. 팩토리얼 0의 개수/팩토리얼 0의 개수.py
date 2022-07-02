cnt = 0
n = int(input())
while n >= 5:
    cnt += n//5
    n //= 5
print(cnt)