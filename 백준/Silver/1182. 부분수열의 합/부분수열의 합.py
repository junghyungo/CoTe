import sys
input = sys.stdin.readline

#=======================================
def backtrack(idx, current_sum, selected):
    # 모든 수를 확인한 경우
    if (idx == n):
        # 현재까지의 합이 S이고, 하나 이상의 원소를 선택한 경우
        if (current_sum == s) and (selected > 0):
            count[0] += 1
        return
    
    # 현재 수를 선택하는 경우
    backtrack(idx+1, current_sum+arr[idx], selected+1)
    
    # 현재 수를 선택하지 않는 경우
    backtrack(idx+1, current_sum, selected)
#=======================================

n, s = map(int, input().split())
arr = list(map(int, input().split()))

# 합이 S가 되는 부분수열의 개수를 저장할 배열
count = [0]
backtrack(0, 0, 0)
print(count[0])