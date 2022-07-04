def fib1(n):
    if n==1 or n==2:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

def fib2(n):
	global cnt
	f = [0]*(n+1)
	f[1] = 1
	f[2] = 1
	for i in range(3, n+1):
		cnt += 1
		f[i] = f[i-1]+f[i-2]
	return cnt
	
n = int(input())
cnt = 0
print(fib1(n), fib2(n))