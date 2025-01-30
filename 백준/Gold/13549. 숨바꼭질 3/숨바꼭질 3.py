from collections import deque

n, k = map(int, input().split())

#=========================
def BFS():
    visited = [0]*100001
    visited[n] = 1
    
    q = deque()
    q.append(n)
    
    while q:
        x = q.popleft()

        # 동생을 만나면
        if (x == k):
            return visited[x]

        # 순간이동한 위치가 범위 안에 있고, 방문하지 않은 곳이면
        if (2*x < 100001) and (visited[2*x] == 0):
            # 0초 소요
            visited[2*x] = visited[x]
            q.append(2*x)

        # 걷기
        for i in (x-1, x+1):
            if (0 <= i < 100001) and (visited[i] == 0):
                # 1초 소요
                visited[i] = visited[x] + 1
                q.append(i)

    return visited[k]
#=========================

print(BFS()-1)