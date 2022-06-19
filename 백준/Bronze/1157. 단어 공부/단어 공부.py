s1 = input().upper()
s2 = list(set(s1))
cnt = []
for i in s2: cnt.append(s1.count(i))
if cnt.count(max(cnt)) > 1: print("?")
else: print(s2[cnt.index(max(cnt))])