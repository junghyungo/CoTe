from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
list_n = list(map(int, input().split()))
m = int(input())
list_m = list(map(int, input().split()))

cnt = Counter(list_n)
for i in list_m:
  print(cnt[i], end=" ")