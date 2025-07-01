import sys
input = sys.stdin.readline

numpad = {
    1: [2, 4],
    2: [1, 3, 5],
    3: [2, 6],
    4: [1, 5, 7],
    5: [2, 4, 6, 8],
    6: [3, 5, 9],
    7: [4, 8, 0],
    8: [5, 7, 9],
    9: [6, 8],
    0: [7]
}

for i in range(int(input())):
    n = int(input())
    dp = [[0]*10 for _ in range(n+1)]

    for i in range(10):
        dp[1][i] = 1

    for i in range(2, n+1):
        for j in range(10):
            for prev in numpad[j]:
                dp[i][j] = dp[i][j] + dp[i-1][prev]

    print(sum(dp[n]) % 1234567)