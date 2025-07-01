import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

dice = [0]*7
up, front, right, left, back, down = 1, 2, 3, 4, 5, 6

# 1 -> 우
# 2 -> 좌
# 3 -> 상
# 4 -> 하
dx = [0, 0,-1, 1]
dy = [1,-1, 0, 0]

for command in commands:
    nx = x + dx[command-1]
    ny = y + dy[command-1]

    if not ((0 <= nx < n) and (0 <= ny < m)):
        continue

    dice_before = dice[:]
    
    if (command == 1):
        dice[down] = dice_before[right]
        dice[right] = dice_before[up]
        dice[up] = dice_before[left]
        dice[left] = dice_before[down]
    elif (command == 2):
        dice[down] = dice_before[left]
        dice[left] = dice_before[up]
        dice[up] = dice_before[right]
        dice[right] = dice_before[down]
    elif (command == 3):
        dice[down] = dice_before[back]
        dice[front] = dice_before[down]
        dice[up] = dice_before[front]
        dice[back] = dice_before[up]
    else:
        dice[down] = dice_before[front]
        dice[back] = dice_before[down]
        dice[up] = dice_before[back]
        dice[front] = dice_before[up]

    if (maps[nx][ny] == 0):
        maps[nx][ny] = dice[down]
    else:
        dice[down] = maps[nx][ny]
        maps[nx][ny] = 0

    print(dice[up])

    x, y = nx, ny