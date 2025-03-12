from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# LIS 배열 (실제 LIS를 저장하는 것이 아니라 길이만 관리)
lis = []

for num in arr:

		# 현재 숫자가 들어갈 위치 탐색
    pos = bisect_left(lis, num)
    
    if (pos == len(lis)):
		    # 새 숫자가 LIS 배열의 끝에 추가됨
        lis.append(num)
    else:
		    # 기존 값과 교체하여 LIS 길이 유지
        lis[pos] = num  

print(len(lis))