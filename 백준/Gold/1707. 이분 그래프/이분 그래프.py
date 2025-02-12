import sys
input = sys.stdin.readline
from collections import deque

#=============================
def BFS(start, group):
    # 시작 정점
    q = deque([start])
    # 시작 정점의 그룹을 설정 (0 / 1)
    visited[start] = group

    while q:
        x = q.popleft()

        # 정점 x에서 갈 수 있는 하위 정점들
        for i in graph[x]:
            # 방문한 정점이 아니라면
            if (visited[i] == 0):
                q.append(i)
                # 상위 정점과 다른 그룹으로 설정
                visited[i] = -1 * visited[x]
            # 방문은 했는데 같은 그룹이면
            elif (visited[i] == visited[x]):
                return 0

    return 1
#=============================

for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [0] * (v+1)

    for _ in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    for i in range(1, v+1):
        # 방문한 정점이 아니였으면 BFS
        if (visited[i] == 0):
            ans = BFS(i, 1)
            if not ans:
                break
    
    print("YES" if ans else "NO")