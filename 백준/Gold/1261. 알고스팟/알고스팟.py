import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
algo = [list(map(int, input().strip())) for _ in range(n)]

dx = [1,-1, 0, 0]
dy = [0, 0, 1,-1]

dist = [[-1]*m for _ in range(n)]
dist[0][0] = 0

q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < m):
            if (dist[nx][ny] == -1):
                # 빈 방이면 -> 앞
                if (algo[nx][ny] == 0):
                    dist[nx][ny] = dist[x][y]
                    q.appendleft((nx, ny))
                # 벽이면 -> 뒤
                else:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

print(dist[n-1][m-1])