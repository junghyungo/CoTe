import sys
input = sys.stdin.readline

n = int(input())
tang = list(map(int, input().split()))

count = {}
left = 0
length = 0

for right in range(n):
    fruit = tang[right]
    count[fruit] = count.get(fruit, 0) + 1

    while (len(count) > 2):
        left_fruit = tang[left]
        count[left_fruit] -= 1

        if (count[left_fruit] == 0):
            del count[left_fruit]

        left += 1

    length = max(length, right-left+1)

print(length)