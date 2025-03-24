import sys
input = sys.stdin.readline

n = int(input())
numbers = [*map(int, input().split())]

visited = [False]*n
selected = [0]*n
max_value = 0

#############################################

def mathematical_expression():
    result = 0
    for i in range(n-1):
        result += abs(selected[i] - selected[i+1])
    return result

#############################################

def backtracking(depth):
    global max_value
    
    if (depth == n):
        max_value = max(max_value, mathematical_expression())
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            selected[depth] = numbers[i]
            backtracking(depth + 1)
            visited[i] = False
    
#############################################

backtracking(0)
print(max_value)