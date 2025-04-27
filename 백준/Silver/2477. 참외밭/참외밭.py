import sys
input = sys.stdin.readline

k = int(input())
lines = [list(map(int, input().split())) for _ in range(6)]

width_idx = []
heigth_idx = []

max_width = 0
max_height = 0

for i in range(6):
    dir, line = lines[i]
    if (dir == 1) or (dir == 2):
        if (line > max_width):
            max_width = line
            width_idx = i
    else:
        if (line > max_height):
            max_height = line
            heigth_idx = i

min_width = abs(lines[(heigth_idx-1)%6][1] - lines[(heigth_idx+1)%6][1])
min_height = abs(lines[(width_idx-1)%6][1] - lines[(width_idx+1)%6][1])
print((max_width*max_height-min_width*min_height)*k)