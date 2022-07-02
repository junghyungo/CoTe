from collections import Counter
for i in range(int(input())):
    arr = []
    for j in range(int(input())):
        n,m = input().split()
        arr.append(m)
    cnt = Counter(arr)
    ans = 1
    for j in cnt:
        ans *= cnt[j]+1
    print(ans-1)