cnt_x = []
cnt_y = []
for i in range(3):
  x,y = map(int, input().split())
  cnt_x.append(x)
  cnt_y.append(y)
for i in range(3):
  if cnt_x.count(cnt_x[i]) == 1: a = cnt_x[i]
  if cnt_y.count(cnt_y[i]) == 1: b = cnt_y[i]
print(a,b)