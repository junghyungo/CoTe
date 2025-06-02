import sys
input = sys.stdin.readline
import heapq

n, m , x = map(int, input().split())

graph_forward = [[] for _ in range(n+1)]
graph_reverse = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    graph_forward[start].append((end, cost))
    graph_reverse[end].append((start, cost))

def dijkstra(start, graph):
    dist = [float("inf")] * (n+1)
    q = []
    heapq.heappush(q, (start, 0))

    while q:
        destination, weight = heapq.heappop(q)

        if (dist[destination] < weight):
            continue

        for next, c in graph[destination]:
            if (dist[next] > weight+c):
                dist[next] = weight+c
                heapq.heappush(q, (next, weight+c))

    return dist

nodes_to_x = dijkstra(x, graph_reverse)
x_to_nodes = dijkstra(x, graph_forward)

answer = []
for i in range(1, n+1):
    if (i != x):
        answer.append(nodes_to_x[i] + x_to_nodes[i])

print(max(answer))