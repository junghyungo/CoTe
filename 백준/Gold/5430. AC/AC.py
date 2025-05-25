import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

for i in range(t):
    p = input()
    n = int(input())
    arr_input = input().strip()

    if (n == 0):
        arr = deque()
    else:
        arr = deque(arr_input[1:-1].split(","))

    R_count = 0
    D_count = 0

    for function in p:
        if (function == "D"):
            D_count += 1
    if (D_count > n):
        print("error")
        continue

    is_error = False
    
    for function in p:
        if (function == "R"):
            R_count += 1
            
        elif (function == "D"):
            if not arr:
                is_error = True
                print("error")
                break
            else:
                if (R_count%2 == 0):
                    arr.popleft()
                else:
                    arr.pop()

    if not is_error:
        if (R_count%2 != 0):
            arr.reverse()
        print("[" + ",".join(arr)  + "]")