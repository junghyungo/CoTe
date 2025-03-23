import sys
input = sys.stdin.readline

n = int(input())
numbers = [*map(int, input().split())]
operators = [*map(int, input().split())]

add = operators[0]
sub = operators[1]
mul = operators[2]
div = operators[3]

max_value = -1000000000
min_value = 1000000000

#========================================
def backtracking(depth, result, add, sub, mul, div):
    global max_value, min_value
    
    if (depth == n):
        max_value = max(max_value, result)
        min_value = min(min_value, result)
        return

    if (add > 0):
        backtracking(depth+1, result+numbers[depth], add-1, sub, mul, div)
    if (sub > 0):
        backtracking(depth+1, result-numbers[depth], add, sub-1, mul, div)
    if (mul > 0):
        backtracking(depth+1, result*numbers[depth], add, sub, mul-1, div)
    if (div > 0):
        if (result < 0):
            backtracking(depth+1, -(-result//numbers[depth]), add, sub, mul, div-1)
        else:
            backtracking(depth+1, result//numbers[depth], add, sub, mul, div-1)
            
#========================================

backtracking(1, numbers[0], add, sub, mul, div)

print(max_value)
print(min_value)