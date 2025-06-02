import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())
ladders = [[False]*(n+1) for _ in range(h+1)]

# 기존 가로선 입력
for i in range(m):
    a, b = map(int, input().split())
    ladders[a][b] = True

# 사다리 타기, i -> i로 잘 가는지 확인
def goal_check():
    for start in range(1, n+1):
        j = start

        for i in range(1, h+1):
            if (ladders[i][j]):      # 오른쪽
                j += 1
            elif (ladders[i][j-1]):  # 왼쪽
                j -= 1

        if (j != start):
            return False

    return True

# 백트래킹, 사다리 추가
def dfs(count, x, y):
    global answer

    if (count >= answer):
        return

    if goal_check():
        answer = count
        return

    for i in range(x, h+1):
        for j in range(1, n):
            if (ladders[i][j] or ladders[i][j-1] or ladders[i][j+1]):
                continue

            ladders[i][j] = True
            dfs(count+1, i, j)
            ladders[i][j] = False # 놓았던 사다리 제거

answer = 4
dfs(0, 1, 1)
print(answer if answer<4 else -1)