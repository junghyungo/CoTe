def dfs(s):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(s, n+1):
        if i not in arr:
            arr.append(i)
            dfs(i+1)
            arr.pop()
			
n,m = list(map(int, input().split()))
arr = []
dfs(1)