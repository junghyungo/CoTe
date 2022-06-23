a,b,v = map(int, input().split())
d = (v-b)/(a-b)
print(int(d) if d%1==0 else int(d)+1)