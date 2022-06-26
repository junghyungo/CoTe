def countPrime(num):
    if num == 1: 
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0: 
            return False
    return True
        
pList = list(range(2, 123456*2))
aList = []
for i in pList:
    if countPrime(i):
        aList.append(i)

while True:
    n = int(input())
    cnt = 0
    if n == 0: break
    for i in aList:
        if n<i<2*n+1:
            cnt += 1
    print(cnt)