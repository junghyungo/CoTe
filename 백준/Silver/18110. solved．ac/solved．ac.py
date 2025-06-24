import sys
input = sys.stdin.readline

n = int(input())

if (n == 0):
    print(0)
else:
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    
    num = int(n*0.15 + 0.5)
    length = n-2*num
    avg = sum(arr[num:n-num]) / length
    print(int(avg + 0.5))