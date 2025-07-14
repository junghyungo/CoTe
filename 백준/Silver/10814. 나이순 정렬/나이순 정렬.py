import sys
input = sys.stdin.readline

n = int(input())
members = [list(input().split()) for _ in range(n)]
members.sort(key=lambda x: int(x[0]))

for i in range(n):
    print(members[i][0], members[i][1])