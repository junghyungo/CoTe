import sys
input = sys.stdin.readline
import heapq

n = int(input())
pq = []

for _ in range(n):
    x = int(input())

    # x 입력
    if (x != 0):
        heapq.heappush(pq, (abs(x), x))

    # 0 입력
    else:
        if pq:
            print(heapq.heappop(pq)[1])
        else:
            print(0)