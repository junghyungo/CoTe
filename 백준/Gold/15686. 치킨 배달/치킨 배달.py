import sys
input = sys.stdin.readline

n, m = map(int, input().split())
city = [[*map(int, input().split())] for _ in range(n)]

house_position = []
chicken_position = []

selected_chickens = []

final_distance = 50*50

for r in range(n):
    for c in range(n):
        if (city[r][c] == 1):
            house_position.append((r, c))
        elif (city[r][c] == 2):
            chicken_position.append((r, c))

#################################################

def chicken_distance():
    total_distance = 0
    for hx, hy in house_position:
        distance = 50*50
        for cx, cy in selected_chickens:
            distance = min(distance, abs(hx-cx) + abs(hy-cy))
        total_distance += distance
    return total_distance

#################################################

def backtracking(index, count):
    global final_distance

    if (count == m):
        final_distance = min(final_distance, chicken_distance())
        return

    for i in range(index, len(chicken_position)):
        selected_chickens.append(chicken_position[i])
        backtracking(i+1, count+1)
        selected_chickens.pop()

#################################################

backtracking(0, 0)
print(final_distance)