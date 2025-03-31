import sys
input = sys.stdin.readline

#########################################################

def calculate_stat(team, s):
    power = 0
    
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            power += s[team[i]][team[j]] + s[team[j]][team[i]]

    return power
    
#########################################################

def backtracking(index, selected, n, s, visited, diff):
    
    # 팀이 절반(N/2)만큼 선택된 경우
    if (len(selected) == n//2):
        # 나머지 팀 구하기
        other_team = [i for i in range(n) if i not in selected]

        # 능력치 계산
        start_power = calculate_stat(selected, s)
        link_power = calculate_stat(other_team, s)

        # 최솟값 갱신
        diff[0] = min(diff[0], abs(start_power-link_power))
        return
    
    # 탐색
    for i in range(index, n):
        if not visited[i]:
            visited[i] = True
            selected.append(i)
            backtracking(i+1, selected, n, s, visited, diff)
            visited[i] = False
            selected.pop()

#########################################################

n = int(input())
s = [[*map(int, input().split())] for _ in range(n)]

visited = [False] * n
diff = [float('inf')]

backtracking(0, [], n, s, visited, diff)

print(diff[0])