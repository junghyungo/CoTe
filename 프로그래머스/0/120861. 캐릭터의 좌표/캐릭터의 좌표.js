function solution(keyinput, board) {
    let x = 0;
    let y = 0;

    const xLimit = Math.floor(board[0] / 2);
    const yLimit = Math.floor(board[1] / 2);

    for (const move of keyinput) {
        switch (move) {
            case 'up':
                if (y < yLimit) {
                    y++;
                }
                break;
            case 'down':
                if (y > -yLimit) {
                    y--;
                }
                break;
            case 'left':
                if (x > -xLimit) {
                    x--;
                }
                break;
            case 'right':
                if (x < xLimit) {
                    x++;
                }
                break;
        }
    }

    return [x, y];
}