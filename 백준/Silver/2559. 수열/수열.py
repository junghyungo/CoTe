import sys
input = sys.stdin.readline

n,k = map(int, input().split())
arr = list(map(int, input().split()))
num = sum(arr[:k])
ans = [num]

for i in range(n-k):
	num = num-arr[i]+arr[i+k]
	ans.append(num)

print(max(ans))