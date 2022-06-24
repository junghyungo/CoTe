n = int(input())
if n>1:
    i = 2
    while n>=i:
        if n%i == 0:
            print(i)
            n = n/i
        else:
            i += 1