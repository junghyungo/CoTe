n = int(input())

mat = list()
for i in range(n):
    mat.append(list(map(int, input().split())))

mat.sort()

for i in range(n):
    print(mat[i][0], mat[i][1])