def dfs(s):
	if len(arr) == m:
		print(' '.join(map(str, arr)))
		return
	for i in range(s, n+1):
		arr.append(i)
		dfs(i)
		arr.pop()
			
n,m = list(map(int, input().split()))
arr = []
dfs(1)