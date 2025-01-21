#============================
from collections import deque

dx = [0, 0, 1,-1]
dy = [1,-1, 0, 0]

def BFS(graph, a, b):
    q = deque()
    q.append((a, b))
    # bfs가 지나가면 0으로 바꾸기
    graph[a][b] = 0

    cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            # 상하좌우로 이동한 좌표
            nx = x + dx[i]
            ny = y + dy[i]

            # 이동한 좌표가 행렬을 벗어난 경우는 제외 (좌표가 음수거나, 가로/세로 길이보다 같거나 큰 경우)
            if (nx < 0) or (nx >= n) or (ny < 0) or (ny >= n):
                continue
            # 이동한 좌표가 이미 배추가 있는 상태면, 0으로 만들고, queue에 담기
            elif (graph[nx][ny] == 1):
                graph[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1

    return cnt
#============================

n = int(input())
table = [list(map(int, input())) for _ in range(n)]

ans = []

for x in range(n):
    for y in range(n):
        if (table[x][y] == 1):
            ans.append(BFS(table, x, y))

ans.sort()
print(len(ans))
print(*ans, sep='\n')