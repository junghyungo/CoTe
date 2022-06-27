n = int(input())
chap = cnt = 0
while True:
    chap += 1
    if("666" in str(chap)):
        cnt += 1
        if cnt == n:
            print(chap)
            break