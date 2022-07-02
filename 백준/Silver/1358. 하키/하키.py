cnt = 0
w,h,x,y,p = map(int, input().split())
for i in range(p):
    px,py = map(int, input().split())
    if x<=px<=x+w and y<=py<=y+h:
        cnt += 1
    elif (x-px)**2+(y+h/2-py)**2 <= (h/2)**2:
        cnt += 1
    elif (x+w-px)**2+(y+h/2-py)**2 <= (h/2)**2:
        cnt += 1
print(cnt)