n = int(input())
naturals = map(int, input().split())
cnt = 0
for i in naturals:
    ex = 0
    if i!=1:
        for j in range(2,i):
            if i%j == 0:
                ex += 1
        if ex == 0:
            cnt += 1
print(cnt)