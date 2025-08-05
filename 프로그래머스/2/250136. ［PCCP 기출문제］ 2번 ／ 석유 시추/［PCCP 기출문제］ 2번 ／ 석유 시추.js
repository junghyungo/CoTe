function solution(land) {
    let answer = 0;
    
    const n = land.length;
    const m = land[0].length;
    
    let oil = Array(n).fill().map(() => Array(m).fill(-1));
    let oilIdx = 0;
    let oilMap = new Map();
    
    let visited = Array(n).fill().map(() => Array(m).fill(false));
    
    const sichu = (i, j, oilidx) => {
        let queue = [];
        
        visited[i][j] = true;
        queue.push([i, j]);
        let cnt = 1;
        
        while (queue.length) {
            const [i, j] = queue.shift();
            oil[i][j] = oilIdx;
            
            for (let [dx, dy] of [[0,1],[1,0],[-1,0],[0,-1]]) {
                const nx = i + dx;
                const ny = j + dy;
                
                if ((0<=nx && nx<n && 0<=ny && ny<m) && !visited[nx][ny] && (land[nx][ny] === 1)) {
                    queue.push([nx, ny]);
                    visited[nx][ny] = true;
                    cnt++;
                }
            }
        }
        
        return cnt;
    }
    
    for (let i=0 ; i<n ; i++) {
        for (let j=0 ; j<m ; j++) {
            if (!visited[i][j] && land[i][j] === 1) {
                const cnt = sichu(i, j, oilIdx);
                oilMap.set(oilIdx, cnt);
                oilIdx++;
            }
        }
    }
    
    for (let j=0 ; j<m ; j++) {
        let tmp = [];
        let sum = 0;
        
        for (let i=0 ; i<n ; i++) {
            if ((oil[i][j] >=0) && (!tmp.includes(oil[i][j]))) {
                const idx = oil[i][j];
                tmp.push(idx);
                sum += oilMap.get(idx);
            }
        }
        
        answer = answer < sum ? sum : answer;
    }
    
    return answer;
}