// n, m: 격자 크기
// x, y: 시작 위치
// r, c: 도착 위치
// k: 총 이동해야 하는 거리
function solution(n, m, x, y, r, c, k) {

    // 1. 초기 필터링: k 내에 목적지 도달이 불가능한 경우
    // 현재 위치에서 목적지까지의 최단 거리(맨해튼 거리) 계산
    const distance = Math.abs(x - r) + Math.abs(y - c);

    // k가 최단 거리보다 작거나, k와 최단 거리의 홀/짝이 다르면 절대 도달 불가
    // (k에서 최단거리를 뺀 값은 추가로 왕복해야 하는 거리이므로 짝수여야 함)
    if (k < distance || (k - distance) % 2 !== 0) {
        return "impossible";
    }

    let answer = '';
    let currentX = x;
    let currentY = y;

    // 이동 방향 우선순위: d(아래), l(왼쪽), r(오른쪽), u(위) -> 알파벳 순서
    const dx = [1, 0, 0, -1]; // d, l, r, u
    const dy = [0, -1, 1, 0];
    const dirs = ['d', 'l', 'r', 'u'];

    // 2. k번 이동하면서 경로 생성
    for (let i=0 ; i<k ; i++) {
        // d, l, r, u 순서로 시도
        for (let j=0 ; j<4 ; j++) {
            const nextX = currentX + dx[j];
            const nextY = currentY + dy[j];

            // (1) 격자 범위 확인
            if (nextX>0 && nextX<=n && nextY>0 && nextY<=m) {
                // (2) 남은 이동 횟수로 목적지에 도달 가능한지 확인
                const distToTarget = Math.abs(nextX - r) + Math.abs(nextY - c);
                const remainingMoves = k - (i + 1);
                
                if (distToTarget <= remainingMoves) {
                    // 현재 방향으로 이동 확정
                    answer += dirs[j];
                    currentX = nextX;
                    currentY = nextY;
                    break; // 다음 이동(i+1)으로 넘어감
                }
            }
        }
    }

    return answer;
}