n,m = map(int,input().split())

set_a = []
for i in range(n):
    set_a.append(input())

cnt = 0
for i in range(m):
    text = input()
    if text in set_a:
        cnt += 1

print(cnt)