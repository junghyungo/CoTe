def dfs():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, n+1):
        arr.append(i)
        dfs()
        arr.pop()
			
n,m = list(map(int, input().split()))
arr = []
dfs()