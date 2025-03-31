import sys
input = sys.stdin.readline

###############################
def backtracking(row, n, cols, diag_right, diag_left, count):

    # 모든 행에 퀸을 배치하면
    if (row == n):
        count[0] += 1
        return

    for col in range(n):
        if not (cols[col] or diag_right[row+col] or diag_left[row-col]):
            cols[col] = diag_right[row+col] = diag_left[row-col] = True
            backtracking(row+1, n, cols, diag_right, diag_left, count)
            cols[col] = diag_right[row+col] = diag_left[row-col] = False
            
###############################

n = int(input())
cols = [False] * n
diag_right = [False] * 2 * n
diag_left = [False] * 2 * n
count = [0]

backtracking(0, n, cols, diag_right, diag_left, count)
print(count[0])