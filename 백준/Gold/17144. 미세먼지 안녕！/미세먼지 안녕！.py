import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]

# 공기청정기 위치
air = []
for i in range(r):
    if (room[i][0] == -1):
        air.append(i)

# 확산
dx = [1,-1, 0, 0]
dy = [0, 0, 1,-1]

def spread():
    temp = [[0]*c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if (room[x][y] > 0):
                spread_amount = room[x][y] // 5
                count = 0
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    
                    if (0 <= nx < r) and (0 <= ny < c) and (room[nx][ny] != -1):
                        temp[nx][ny] += spread_amount
                        count += 1
                room[x][y] -= spread_amount * count

    for x in range(r):
        for y in range(c):
            room[x][y] += temp[x][y]

def air_clean():
    top = air[0]
    bottom = air[1]

    # 위쪽 (반시계)
    for i in range(top-1, 0, -1):
        room[i][0] = room[i-1][0]
    for i in range(c-1):
        room[0][i] = room[0][i+1]
    for i in range(top):
        room[i][c-1] = room[i+1][c-1]
    for i in range(c-1, 1, -1):
        room[top][i] = room[top][i-1]
    room[top][1] = 0

    # 아래쪽 (시계)
    for i in range(bottom+1, r-1):
        room[i][0] = room[i+1][0]
    for i in range(c-1):
        room[r-1][i] = room[r-1][i+1]
    for i in range(r-1, bottom, -1):
        room[i][c-1] = room[i-1][c-1]
    for i in range(c-1, 1, -1):
        room[bottom][i] = room[bottom][i-1]
    room[bottom][1] = 0

for _ in range(t):
    spread()
    air_clean()

total = 0
for i in range(r):
    for j in range(c):
        if (room[i][j] > 0):
            total += room[i][j]

print(total)