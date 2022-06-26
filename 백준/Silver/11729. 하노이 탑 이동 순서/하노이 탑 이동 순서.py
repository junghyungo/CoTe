def hanoi(num, fromP, toP):
    if num == 1:
        print(fromP, toP)
        return
    hanoi(num-1, fromP, 6-fromP-toP)
    print(fromP, toP)
    hanoi(num-1, 6-fromP-toP, toP)

n = int(input())
print(2**n-1)
hanoi(n, 1, 3)