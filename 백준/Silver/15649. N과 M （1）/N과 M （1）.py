import sys
input = sys.stdin.readline

n, m = map(int, input().split())

#=======================================
def backtrack(n, m, depth, visited, result):
    # 기저 조건: m개의 숫자를 모두 선택한 경우
    if depth == m:
        print(' '.join(map(str, result)))
        return
    
    # 1부터 n까지의 숫자를 탐색
    for i in range(1, n+1):
        # 아직 선택하지 않은 숫자라면
        if not visited[i]:
            visited[i] = True  # 방문 표시
            result.append(i)   # 결과 배열에 추가
            
            # 다음 숫자 선택을 위한 재귀 호출
            backtrack(n, m, depth+1, visited, result)
            
            # 백트래킹: 선택 취소
            visited[i] = False
            result.pop()
#=======================================

visited = [False] * (n+1)
result = []
backtrack(n, m, 0, visited, result)