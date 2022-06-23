cnt = 0
for i in range(int(input())):
    w1 = input()
    for j in range(len(w1)-1):
        if w1[j] != w1[j+1]:
            w2 = w1[j+1:]
            if w1[j] in w2:
                cnt -= 1
                break
    cnt += 1
print(cnt)