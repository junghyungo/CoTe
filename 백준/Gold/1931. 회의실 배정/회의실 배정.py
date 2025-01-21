n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]
arr.sort(key=lambda x : (x[1], x[0]))

ans = []
ans.append(arr[0])
end_time = arr[0][1]

for i in range(1, n):
    if (end_time <= arr[i][0]):
        ans.append(arr[i])
        end_time = arr[i][1]

print(len(ans))