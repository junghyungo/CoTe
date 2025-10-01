function solution(info, edges) {
    // 0: 양, 1: 늑대
    let answer = 0;
    
    // 각 노드의 연결 정보를 저장할 인접 리스트
    const graph = Array.from({ length: info.length }, () => []);
    for (const [parent, child] of edges) {
        graph[parent].push(child);
    }

    /**
     * 깊이 우선 탐색 (DFS) 함수
     * @param {number} currentNode - 현재 노드
     * @param {number} sheep - 현재까지 모은 양의 수
     * @param {number} wolves - 현재까지 모은 늑대의 수
     * @param {number[]} nextNodes - 다음에 방문할 수 있는 노드들의 목록
     */
    function dfs(currentNode, sheep, wolves, nextNodes) {
        // 1. 현재 노드의 동물이 양인지 늑대인지 확인하여 개수 업데이트
        if (info[currentNode] === 0) {
            sheep++;
        } else {
            wolves++;
        }

        // 2. 늑대에게 잡아먹히는 조건인지 확인
        if (sheep <= wolves) {
            return; // 양이 늑대보다 많지 않으면 더 이상 탐색하지 않고 종료
        }

        // 3. 현재까지 모은 양의 수를 정답과 비교하여 갱신
        answer = Math.max(answer, sheep);

        // 4. 다음 탐색 진행
        // 현재 방문 가능한 노드 목록에서 현재 노드를 제외하고,
        // 현재 노드와 연결된 자식 노드들을 추가하여 새로운 방문 목록 생성
        const newNextNodes = [...nextNodes];
        const currentIndex = newNextNodes.indexOf(currentNode);
        newNextNodes.splice(currentIndex, 1); // 현재 노드는 방문했으므로 목록에서 제거
        
        // 현재 노드의 자식들을 다음에 방문할 노드 목록에 추가
        if (graph[currentNode]) {
            newNextNodes.push(...graph[currentNode]);
        }
        
        // 방문 가능한 모든 다음 노드에 대해 재귀적으로 탐색
        for (const nextNode of newNextNodes) {
            dfs(nextNode, sheep, wolves, newNextNodes);
        }
    }

    // 0번 노드(루트)부터 탐색 시작
    // 처음에는 0번 노드만 방문 가능
    dfs(0, 0, 0, [0]); 

    return answer;
}