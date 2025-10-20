function solution(board) {
    const n = board.length;
    const dx = [-1, -1, -1, 0, 0, 1, 1, 1];
    const dy = [-1, 0, 1, -1, 1, -1, 0, 1];
    
    for (let i=0 ; i<n ; i++) {
        for (let j=0 ; j<n ; j++) {
            if (board[i][j] === 1) {
                for (let d = 0; d < 8; d++) {
                    const ni = i + dx[d];
                    const nj = j + dy[d];
                    if (ni>=0 && ni<n && nj>=0 && nj<n && board[ni][nj] === 0) {
                        board[ni][nj] = 2;
                    }
                }
            }
        }
    }
    
    let result = 0;
    
    for (let i=0 ; i<board.length ; i++) {
        for (let j=0 ; j<board.length ; j++) {
            if (board[i][j] === 0)
                result++;
        }
    }
    
    return result;
}