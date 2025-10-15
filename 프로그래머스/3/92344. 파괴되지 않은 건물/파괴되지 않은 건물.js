function solution(board, skill) {
    let result = 0;
    
    const N = board.length;
    const M = board[0].length;
    const changeBoard = Array.from(
        { length: N + 1 },
        () => Array(M + 1).fill(0)
    );
    
    for (const s of skill) {
        let [type, r1, c1, r2, c2, degree] = s;
        if (type === 1) {
            degree *= -1;
        }
        changeBoard[r1][c1] += degree;
        changeBoard[r1][c2 + 1] -= degree;
        changeBoard[r2 + 1][c1] -= degree;
        changeBoard[r2 + 1][c2 + 1] += degree;
    }
    
    for (let i=0 ; i<N ; i++) {
        for (let j=1 ; j<M ; j++) {
            changeBoard[i][j] += changeBoard[i][j - 1];
        }
    }

    for (let j=0 ; j<M ; j++) {
        for (let i=1 ; i<N ; i++) {
            changeBoard[i][j] += changeBoard[i - 1][j];
        }
    }
    
    for (let i=0 ; i<N ; i++) {
        for (let j=0 ; j<M ; j++) {
            board[i][j] += changeBoard[i][j];
            if (board[i][j] > 0) {
                result++;
            }
        }
    }
    
    console.log(board);
    return result;
}