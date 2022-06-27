pos = []
for i in range(int(input())):
    x,y = map(int,input().split())
    pos.append((x,y))
pos.sort()
for i in pos:
    print(i[0], i[1])