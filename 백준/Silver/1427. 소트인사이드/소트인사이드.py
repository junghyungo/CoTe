arr = []
n = input()
for i in range(len(n)): 
    arr.append(n[i])
arr.sort(reverse=True)
for i in arr:
    print(i, end="")