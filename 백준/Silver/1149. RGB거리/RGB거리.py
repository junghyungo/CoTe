import sys
input = sys.stdin.readline

n = int(input())
paint = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * 3 for _ in range(n)]
# 1번 집은 그대로
dp[0] = paint[0]

for i in range(1, n):
    dp[i][0] = paint[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = paint[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = paint[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[n-1]))