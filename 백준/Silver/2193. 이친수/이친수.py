import sys
input = sys.stdin.readline

n = int(input())

if (n == 1) or (n == 2):
    print(1)
else:
    DP = [0]*(n+1)
    DP[1] = 1
    DP[2] = 1

    for i in range(3, n+1):
        DP[i] = DP[i-1] + DP[i-2]

    print(DP[n])