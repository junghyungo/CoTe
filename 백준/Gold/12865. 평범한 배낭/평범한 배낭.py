import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    w, v = map(int, input().split())

    for j in range(k + 1):
        if (j < w):
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j], dp[i][j-w] + v)

print(dp[n][k])