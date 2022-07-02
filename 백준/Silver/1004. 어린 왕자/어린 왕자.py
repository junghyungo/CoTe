for i in range(int(input())):
    x1,y1,x2,y2 = map(int, input().split())
    cnt = 0
    for i in range(int(input())):
        cx,cy,r = map(int, input().split())
        d1 = (x1-cx)**2 + (y1-cy)**2
        d2 = (x2-cx)**2 + (y2-cy)**2
        r = r**2
        if r>d1 and r>d2: pass
        elif r>d1 or r>d2: cnt += 1
    print(cnt)