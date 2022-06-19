s = input()
arr = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
t = 0
for i in range(len(s)):
    for j in arr:
        if s[i] in j:
            t += arr.index(j)+3
print(t)