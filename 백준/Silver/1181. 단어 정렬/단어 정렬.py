arr = []
for i in range(int(input())):
    w = input()
    arr.append((len(w), w))
arr2 = set(arr)
arr = list(arr2)
arr.sort()
for i in arr: print(i[1])