import sys
input = sys.stdin.readline

m = int(input())
s = set()

for _ in range(m):
    temp = input().split()

    if (len(temp) == 1):
        if (temp[0] == 'all'):
            s = set([i for i in range(1, 21)])
        else:
            s = set()
    else:
        calc, x = temp[0], int(temp[1])

        if (calc == 'add'):
            s.add(x)
        elif (calc == 'remove'):
            s.discard(x)
        elif (calc == 'check'):
            print(1 if x in s else 0)
        elif (calc == 'toggle'):
            if (x in s):
                s.discard(x)
            else:
                s.add(x)