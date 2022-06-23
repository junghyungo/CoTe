n = int(input())
cnt = comb = 1
while n>comb:
    comb += cnt*6
    cnt += 1
print(cnt)