import sys
input = sys.stdin.readline

# 최대 입력값을 고려한 DP 테이블 초기화
# (0 <= n <= 40)
dp = [[0, 0] for _ in range(41)]

# 초기값 설정
# fibonacci(0)의 0과 1 출력 횟수
dp[0] = [1, 0]
# fibonacci(1)의 0과 1 출력 횟수
dp[1] = [0, 1]

# 미리 구해놓고 출력
for i in range(2, 41):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

for _ in range(int(input())):
    n = int(input())
    print(dp[n][0], dp[n][1])