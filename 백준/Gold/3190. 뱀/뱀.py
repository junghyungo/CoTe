import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
board = [[0]*(n+1) for _ in range(n+1)]
board[1][1] = 1

k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    board[x][y] = 2

paths = {}
l = int(input())
for _ in range(l):
    x, c = input().split()
    paths[int(x)] = c

time = 0
dx = [1, 0,-1, 0]
dy = [0, 1, 0,-1]
x, y = 1, 1
direction = 0
snake = deque([(1, 1)])

while True:
    nx, ny = x+dx[direction], y+dy[direction]

    if (nx<=0 or nx>n or ny<=0 or ny>n) or ((nx, ny) in snake):
        break

    if (board[ny][nx] != 2):
        a, b = snake.popleft()
        board[b][a] = 0

    x, y = nx, ny
    board[y][x] = 1
    snake.append((x, y))
    time += 1

    if time in paths.keys():
        if paths[time] == "D":
            direction = (direction + 1) % 4
        else:    
            direction = (direction - 1) % 4

print(time+1)