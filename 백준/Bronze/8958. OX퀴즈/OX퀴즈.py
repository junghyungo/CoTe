n = int(input())
for i in range(n):
    result = list(input())
    a = 1
    b = 0
    for j in result:
        if j=="O":
            b += a
            a += 1
        else:
            a = 1
    print(b)