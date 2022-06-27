import sys
arr = []
for i in range(int(input())):
    arr.append(int(sys.stdin.readline()))
for i in sorted(arr):
    sys.stdout.write(str(i)+"\n")