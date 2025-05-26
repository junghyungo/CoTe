import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
map = [[*map(int, input().split())] for _ in range(n)]

result_time = float('inf')
result_height = 0

for height in range(257):
    remove_blocks = 0
    add_blocks = 0

    for i in range(n):
        for j in range(m):
            current_height = map[i][j]
            if (current_height > height):
                # 제거
                remove_blocks += (current_height - height)
            else:
                # 추가
                add_blocks += (height- current_height)

    # 블록 추가가 가능한지 확인
    if (remove_blocks + b < add_blocks):
        continue
        
    time = remove_blocks*2 + add_blocks
    if (time <= result_time):
        result_time = time
        result_height = height

print(result_time, result_height)