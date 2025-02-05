import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
campus = [list(list(input())) for _ in range(n)]

# 도연의 시작 좌표
DY_x, DY_y = 0, 0
for i in range(n):
    for j in range(m):
        # 찾으면 루프 탈출
        if (campus[i][j] == 'I'):
            DY_x, DY_y = i, j
            break
    else:
        continue
    break

#===================================
dx = [0, 0, 1,-1]
dy = [1,-1, 0, 0]

# 방문 리스트를 쓰는 대신, 그래프에 방문 처리
campus[DY_x][DY_y] = 'V' # Visited
q = deque([(DY_x, DY_y)])
ans = 0

while q:
    x, y = q.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        

        if (0 <= nx < n) and (0 <= ny < m) and (campus[nx][ny] not in ('X', 'V')):            
            # 사람 발견시
            if (campus[nx][ny] == 'P'):
                ans += 1    
                
            # 방문 처리
            campus[nx][ny] = 'V'
            q.append((nx, ny))
#===================================

print(ans if (ans > 0) else 'TT')