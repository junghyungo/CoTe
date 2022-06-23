for a in range(int(input())):
    k = int(input())
    n = int(input())
    ff = [x for x in range(1,n+1)]
    for b in range(k): 
        for c in range(1,n):
            ff[c] += ff[c-1]
    print(ff[-1])