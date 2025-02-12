import sys
import itertools
from collections import deque

input = sys.stdin.readline

# 상, 하, 좌, 우 이동
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# BFS를 통한 바이러스 확산
def BFS():
    q = deque(virus_positions)
    tmp_graph = [row[:] for row in graph]  # deepcopy 대신 리스트 슬라이싱 사용

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                q.append((nx, ny))

    # 안전 영역 크기 계산
    global ans
    safe_area = sum(row.count(0) for row in tmp_graph)
    ans = max(ans, safe_area)

# 벽을 세울 모든 조합 탐색
def solve():
    global ans
    for walls in itertools.combinations(empty_spaces, 3):
        # 벽 세우기
        for x, y in walls:
            graph[x][y] = 1
        
        BFS()  # 바이러스 확산 후 안전 영역 계산

        # 벽 되돌리기
        for x, y in walls:
            graph[x][y] = 0

# 입력 받기
n, m = map(int, input().split())
graph = []
empty_spaces = []  # 벽을 세울 수 있는 공간들
virus_positions = []  # 초기 바이러스 위치들
ans = 0

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(m):
        if row[j] == 0:
            empty_spaces.append((i, j))
        elif row[j] == 2:
            virus_positions.append((i, j))

solve()
print(ans)