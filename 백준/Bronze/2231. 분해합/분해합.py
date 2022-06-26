n = int(input())
sum = 0
for i in range(1, n+1):
    dec = 0
    m = list(map(int, str(i)))
    for j in m: dec += j
    dec += i
    sum += dec
    if dec == n: 
        print(i)
        break
    if i == n:
        print(0)