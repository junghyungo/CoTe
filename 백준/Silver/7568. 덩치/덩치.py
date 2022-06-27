n = int(input())
data = []
rate = []

for i in range(n):
    kg,cm = map(int, input().split())
    data.append((kg,cm))

for i in range(len(data)):
    cnt = 0
    for j in range(len(data)):
        if data[i][0]<data[j][0] and data[i][1]<data[j][1]:
            cnt += 1
    rate.append(cnt+1)

for i in rate: print(i, end=" ")