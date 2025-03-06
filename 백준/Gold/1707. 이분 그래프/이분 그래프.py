import sys
input = sys.stdin.readline
from collections import deque

k = int(input().strip())

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]

    for _ in range(e):
        u, w = map(int, input().split())
        # 무방향 그래프
        graph[u].append(w)
        graph[w].append(u)

    visited = [-1] * (v+1)
    queue = deque()
    ans = True

    for i in range(1, v+1):
        if (visited[i] == -1):
            queue.append(i)
            visited[i] = 0

            while queue:
                node = queue.popleft()

                for j in graph[node]:
                    if (visited[j] == -1):
                        visited[j] = 1 - visited[node]
                        queue.append(j)
                    elif (visited[j] == visited[node]):
                        ans = False
                        break

                if not ans:
                    break

        if not ans:
            break
            
    print('YES' if ans else 'NO')