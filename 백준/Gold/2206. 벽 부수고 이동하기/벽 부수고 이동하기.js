const fs = require('fs');
const filePath = '/dev/stdin';
const input = fs.readFileSync(filePath).toString().trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);
const map = input.slice(1).map(rowString => 
    rowString.split('').map(Number)
);

function solution(N, M, map) {
    // visited[x][y][0]: 벽 안 부수고 온 최단 거리
    // visited[x][y][1]: 벽 1개 부수고 온 최단 거리
    const visited = [];
    for (let i=0 ; i<N ; i++) {
        const row = [];
        for (let j=0 ; j<M ; j++) {
            row.push([0, 0]);
        }
        visited.push(row);
    }

    const queue = [];
    let queueIndex = 0;

    const dx = [0, 0, 1, -1];
    const dy = [1, -1, 0, 0];

    // [x, y, (0: 안부숨, 1: 부숨)]
    queue.push([0, 0, 0]);
    visited[0][0][0] = 1;

    // BFS 시작
    while (queue.length > queueIndex) {
        const [x, y, broken] = queue[queueIndex++];

        for (let i=0 ; i<4 ; i++) {
            const nx = x + dx[i];
            const ny = y + dy[i];

            if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
                continue;
            }

            // 다음 칸이 0
            if (map[nx][ny] === 0 && visited[nx][ny][broken] === 0) {
                visited[nx][ny][broken] = visited[x][y][broken] + 1;
                queue.push([nx, ny, broken]);
            }
    
            // 다음 칸이 1이고, 아직 벽을 안 부순 경우
            if (map[nx][ny] === 1 && broken === 0 && visited[nx][ny][1] === 0) {
                visited[nx][ny][1] = visited[x][y][0] + 1;
                queue.push([nx, ny, 1]);
            }
        }
    }

    const resultA = visited[N-1][M-1][0];
    const resultB = visited[N-1][M-1][1];
      
    if (resultA === 0 && resultB === 0) {
        return -1;
    } else if (resultA === 0) {
        return resultB;
    } else if (resultB === 0) {
        return resultA;
    } else {
        return Math.min(resultA, resultB);
    }
}

console.log(solution(N, M, map));