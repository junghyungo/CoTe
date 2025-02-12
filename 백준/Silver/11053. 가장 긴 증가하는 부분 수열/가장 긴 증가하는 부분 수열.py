import sys
input = sys.stdin.readline

def longest_increasing_subsequence(n, arr):
    dp = [1] * n  # 모든 원소는 길이 1의 LIS로 시작

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:  # 증가하는 관계일 때
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)  # 가장 긴 부분 수열의 길이 반환

n = int(input())
arr = list(map(int, input().split()))

# 모든 원소는 길이 1로 시작
DP = [1]*n

for i in range(n):
    for j in range(i):
        # 증가할 때
        if (arr[j] < arr[i]):
            DP[i] = max(DP[i], DP[j]+1)

print(max(DP))