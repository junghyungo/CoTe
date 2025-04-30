import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

board = [i for i in range(101)]
for _ in range(n + m):
    a, b = map(int, input().split())
    board[a] = b

visited = [False] * 101
dist = [0] * 101
q = deque([1])
visited[1] = True

while q:
    current = q.popleft()

    for dice in range(1, 7):
        next = current + dice
        if (next > 100):
            continue

        next = board[next]

        if not visited[next]:
            visited[next] = True
            dist[next] = dist[current] + 1

            if (next == 100):
                print(dist[100])
                exit()

            q.append(next)