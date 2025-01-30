from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

# 인접리스트로 그래프 초기화
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0]*(n+1)
cnt = 0

# 1번 노드부터
for i in range(1, n+1):
    # 방문한 적이 없으면
    if not visited[i]:
        #=============BFS====================
        # append 없이 한줄로 Queue 만들고 초기값 넣기
        q = deque([i])
        # 방문 처리
        visited[i] = 1

        while q:
            node = q.popleft()

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = 1
                    q.append(neighbor)
        #====================================
        cnt += 1

print(cnt)