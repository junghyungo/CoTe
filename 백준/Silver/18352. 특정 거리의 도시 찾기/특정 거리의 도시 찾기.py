import sys
input = sys.stdin.readline
import heapq

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

dist = [float('inf')] * (n+1)
dist[x] = 0

h = []
heapq.heappush(h, (0, x)) # (거리,노드)

while h:
    distance, current = heapq.heappop(h)

    if (distance > dist[current]):
        # 이미 더 짧은 거리로 방문한 경우
        continue

    for neighbor, weight in graph[current]:
        cost = distance + weight
        if (cost < dist[neighbor]):
            dist[neighbor] = cost
            heapq.heappush(h, (cost, neighbor))

result = [i for i in range(1, n+1) if (dist[i] == k)]

if (result):
    for city in sorted(result):
        print(city)
else:
    print(-1)