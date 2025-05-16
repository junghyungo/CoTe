import sys
input = sys.stdin.readline
import heapq

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

#===============================
distance = [float('inf')] * (n+1)
distance[start] = 0

q = []
heapq.heappush(q, (0, start)) # 비용, 시작도시

while q:
    dist, current = heapq.heappop(q)

    if (distance[current] < dist):
        continue

    for next, cost in graph[current]:
        new_cost = dist + cost

        if (new_cost < distance[next]):
            distance[next] = new_cost
            heapq.heappush(q, (new_cost, next))

#===============================

print(distance[end])