import sys
input = sys.stdin.readline
import heapq

n, d = map(int, input().split())

graph = [[] for _ in range(d+1)]

# 고속도로
for i in range(d):
    graph[i].append((i+1, 1))

# 지름길
for _ in range(n):
    start, end, cost = map(int, input().split())
    if (end <= d):
        graph[start].append((end, cost))

dist = [float('inf')] * (d+1)
dist[0] = 0
h = [(0, 0)]

while h:
    distance, current = heapq.heappop(h)

    if (dist[current] < distance):
        continue

    for next, weight in graph[current]:
        cost = distance + weight
        if (cost < dist[next]):
            dist[next] = cost
            heapq.heappush(h, (cost, next))

print(dist[d])