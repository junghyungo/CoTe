import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
cards = [input().strip() for _ in range(n)]

visited = [False]*n
nums = set()

########################################

def backtracking(depth, num):
    if (depth == k):
        nums.add(num)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            backtracking(depth+1, num+cards[i])
            visited[i] = False

########################################

backtracking(0, "")
print(len(nums))