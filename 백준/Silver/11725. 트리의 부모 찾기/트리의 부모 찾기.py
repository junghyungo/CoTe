from collections import deque

n = int(input())

tree = [[] for i in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# 루트 노드 1을 큐에 추가
q = deque()
q.append(1)

ans = [0] * (n+1)

#======================
# BFS
while q:
    node = q.popleft()
            
    # 현재 노드와 연결된 노드들에 대해
    for edged_node in tree[node]:
        # 방문을 안 했으면
        if ans[edged_node] == 0:
            ans[edged_node] = node
            q.append(edged_node)
#======================

# 2번 노드부터 출력
for i in ans[2:]:
    print(i)