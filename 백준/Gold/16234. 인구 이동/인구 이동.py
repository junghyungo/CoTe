import sys
input = sys.stdin.readline
from collections import deque

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [ 0, 0,-1, 1]

# 연합찾기
def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    union = [(x, y)]
    population = graph[x][y]

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if (0 <= nx < n) and (0 <= ny < n) and (not visited[nx][ny]):
                if (l <= abs(graph[x][y] - graph[nx][ny]) <= r):
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    union.append((nx, ny))
                    population += graph[nx][ny]

    if (len(union) > 1):
        new_population = population // len(union)
        for x, y in union:
            graph[x][y] = new_population
        return True
        
    return False

day = 0
while True:
    visited = [[False]*n for _ in range(n)]
    moved = False

    for i in range(n):
        for j in range(n):
            if (not visited[i][j]):
                if bfs(i, j, visited):
                    moved = True

    if (not moved):
        break
    day += 1

print(day)