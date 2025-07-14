import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(node, dist):
    visited[node] = True

    for neighbor, weight in tree[node]:
        if not visited[neighbor]:
            distance[neighbor] = dist + weight
            dfs(neighbor, dist + weight)

n = int(input())

tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))
    tree[child].append((parent, weight))

visited = [False] * (n+1)
distance = [0] * (n+1)
dfs(1, 0)
a = distance.index(max(distance))

visited = [False] * (n+1)
distance = [0] * (n+1)
dfs(a, 0)

print(max(distance))