n = int(input())
arr = sorted([*map(int, input().split())])

ans = []
current = 0

for i in arr:
    current += i
    ans.append(current)

print(sum(ans))