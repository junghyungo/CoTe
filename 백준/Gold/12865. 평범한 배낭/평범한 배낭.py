import sys
input = sys.stdin.readline

n, k = map(int, input().split())

bag = []
dp = [0] * (k+1)

for _ in range(n):
    w, v = map(int, input().split())
    bag.append((w, v))

for w, v in bag:
    for i in range(k, w-1, -1):
        dp[i] = max(dp[i], dp[i-w] + v)

print(dp[k])