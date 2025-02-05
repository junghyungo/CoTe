from collections import deque
import sys
input = sys.stdin.readline

#=====================================
def BFS(l, start_x, start_y, end_x, end_y):

    # 상좌, 상우 / 하좌, 하우 / 좌상, 좌하 / 우상, 우하
    dx = [-1, 1,-1, 1,-2,-2, 2, 2]
    dy = [-2,-2, 2, 2, 1,-1, 1,-1]
    
    if (start_x == end_x) and (start_y == end_y):
        return 0

    q = deque([(start_x, start_y, 0)])
    visited = [[0]*l for _ in range(l)]
    visited[start_x][start_y] = 1

    while q:
        x, y, cnt = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0<=nx<l) and (0<=ny<l):
                if (nx == end_x) and (ny == end_y):
                    return (cnt+1)
                elif (visited[nx][ny] == 0):
                    visited[nx][ny] = 1
                    q.append((nx, ny, cnt+1))
#=====================================

for _ in range(int(input())):
    l = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    print(BFS(l, start_x, start_y, end_x, end_y))