import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()

i = 0
cnt = 0
ans = 0

while i < m - 1:
    if s[i:i+3] == 'IOI':
        cnt += 1
        i += 2
        if cnt == n:
            ans += 1
            cnt -= 1  # 겹치는 경우 고려
    else:
        i += 1
        cnt = 0

print(ans)