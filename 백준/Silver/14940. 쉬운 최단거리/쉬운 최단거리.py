import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 2와의 거리 (초기값 -1)
ans = [[-1]*m for _ in range(n)]

#===================================
# 2와 갈 수 없는곳 찾기
q = deque()
for i in range(n):
    for j in range(m):
        if (graph[i][j] == 2):
            q.append((i, j))
            ans[i][j] = 0
        elif (graph[i][j] == 0):
            ans[i][j] = 0
            
dx = [0, 0, 1,-1]
dy = [1,-1, 0, 0]

while q:
    x, y = q.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 갈 수 있는 땅이고, 아직 도달 안 한 곳이면
        if (0 <= nx < n) and (0 <= ny < m) and (graph[nx][ny] == 1) and (ans[nx][ny] == -1):            
            ans[nx][ny] = ans[x][y] + 1
            q.append((nx, ny))
#===================================

for i in ans:
    print(*i)