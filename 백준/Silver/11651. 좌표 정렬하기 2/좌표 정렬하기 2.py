arr1 = []
for i in range(int(input())):
    x,y = map(int,input().split())
    arr1.append((y,x))
arr2 = sorted(arr1)
for i in arr2:
    print(i[1], i[0])