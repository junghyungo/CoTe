import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1,-1, 0, 0]
dy = [0, 0, 1,-1]

# 아기상어 초기 위치
for i in range(n):
    for j in range(n):
        if (graph[i][j] == 9):
            x, y = i, j
            graph[i][j] = 0  # 초기 위치는 빈 칸으로 처리

size = 2  # 아기 상어 크기
eaten = 0  # 먹은 물고기 수
time = 0  # 시간

# BFS로 가장 가까운 먹을 수 있는 물고기 탐색
def bfs(x, y, size):
    visited = [[-1] * n for _ in range(n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    fishes = []

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < n) and (visited[nx][ny] == -1):
                # 이동 가능한 경우 (작거나 같을 때)
                if graph[nx][ny] <= size:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

                    # 먹을 수 있는 물고기
                    if 0 < graph[nx][ny] < size:
                        fishes.append((visited[nx][ny], nx, ny))

    # 거리, 위쪽, 왼쪽 순 정렬
    fishes.sort()
    return fishes

while True:
    fish_list = bfs(x, y, size)

    if not fish_list:  # 더 이상 먹을 수 있는 물고기 없음
        break

    dist, nx, ny = fish_list[0]  # 가장 가까운 물고기
    time += dist
    eaten += 1
    graph[nx][ny] = 0  # 물고기 먹기
    x, y = nx, ny  # 상어 위치 이동

    if eaten == size:
        size += 1
        eaten = 0

print(time)