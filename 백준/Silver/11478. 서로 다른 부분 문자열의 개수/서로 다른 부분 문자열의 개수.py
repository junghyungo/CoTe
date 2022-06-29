s = input()
cnt = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        tmp = s[i : j+1]
        cnt.add(tmp)
      
print(len(cnt))