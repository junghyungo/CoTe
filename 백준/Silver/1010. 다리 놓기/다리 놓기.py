for i in range(int(input())):
    n,m = map(int, input().split())
    n = min(n, m-n)
    a = 1
    b = 1
    for i in range(n):
        a *= m
        m -= 1
        b *= n
        n -= 1
    print(a//b)