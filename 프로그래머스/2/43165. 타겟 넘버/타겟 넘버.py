def dfs(depth, sum, numbers, target):
    global answer
    
    if (depth == len(numbers)):
        if (sum == target):
            answer += 1
        return
    
    dfs(depth+1, sum+numbers[depth], numbers, target)
    dfs(depth+1, sum-numbers[depth], numbers, target)

def solution(numbers, target):
    global answer
    answer = 0
    dfs(0, 0, numbers, target)
    print(answer)
    
    return answer