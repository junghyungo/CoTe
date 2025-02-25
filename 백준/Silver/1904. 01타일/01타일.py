import sys
input = sys.stdin.readline

n = int(input())

if (n == 1):
    print(1)
elif (n == 2):
    print(2)
else:
    prev_2 = 1
    prev_1 = 2

    for _ in range(3, n+1):
        current = (prev_1 + prev_2) % 15746
        prev_2 = prev_1
        prev_1 = current

    print(prev_1)