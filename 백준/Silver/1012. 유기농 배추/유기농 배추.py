#============================
from collections import deque

dx = [0, 0, 1,-1]
dy = [1,-1, 0, 0]

def BFS(graph, a, b):
    q = deque()
    q.append((a, b))
    # bfs가 지나가면 0으로 바꾸기
    graph[a][b] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            # 상하좌우로 이동한 좌표
            nx = x + dx[i]
            ny = y + dy[i]

            # 이동한 좌표가 행렬을 벗어난 경우는 제외 (좌표가 음수거나, 가로/세로 길이보다 같거나 큰 경우)
            if (nx < 0) or (nx >= n) or (ny < 0) or (ny >= m):
                continue
            # 이동한 좌표가 이미 배추가 있는 상태면, 0으로 만들고, queue에 담기
            elif (graph[nx][ny] == 1):
                graph[nx][ny] = 0
                q.append((nx, ny))
#============================

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    # 밭 생성
    field = [[0]*m for x in range(n)]
    
    for i in range(k):
        x, y = map(int, input().split())
        # 배추 심기
        field[y][x] = 1
    
    # 배추 심은곳 묶음 만들기
    cnt = 0

    for x in range(n):
        for y in range(m):
            # 배추가 있는 부분 찾아서 BFS 진행
            if (field[x][y] == 1):
                # BFS로 0으로 만들면서 묶음 만들기
                BFS(field, x, y)
                cnt += 1

    print(cnt)