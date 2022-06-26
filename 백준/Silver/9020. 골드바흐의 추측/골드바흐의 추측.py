def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0: 
            return False
    return True

for i in range(int(input())):
    n = int(input())
    a = b = n//2
    while a>1:
        if isPrime(a) and isPrime(b):
            print(a,b)
            break
        else:
            a -= 1
            b += 1