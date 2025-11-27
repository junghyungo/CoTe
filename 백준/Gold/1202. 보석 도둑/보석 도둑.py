import heapq
import sys
input=sys.stdin.readline

def solution():
  n, k = map(int, input().split())

  bosuks = []
  for i in range(1, n+1):
      bosuks.append(list(map(int, input().split())))
  bosuks.sort()

  bags = []
  for i in range(n+1, n+1+k):
      bags.append(int(input()))
  bags.sort()

  result = 0
  tmp = []
  i = 0
  for bag in bags:
      while (i < len(bosuks) and bosuks[i][0] <= bag):
          heapq.heappush(tmp, -bosuks[i][1])
          i += 1
      if len(tmp):
          result -= heapq.heappop(tmp)
  return result

print(solution())