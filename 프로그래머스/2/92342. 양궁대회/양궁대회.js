function solution(n, info) {
    let maxDiff = 0;
    let answer = [-1];

    const dfs = (index, leftArrows, ryanShots) => {
        if (index > 10) {
            const finalRyanShots = [...ryanShots];
            finalRyanShots[10] += leftArrows;

            let ryanScore = 0;
            let apeachScore = 0;
            for (let i = 0; i <= 10; i++) {
                if (finalRyanShots[i] > info[i]) {
                    ryanScore += (10 - i);
                } else if (info[i] > 0) {
                    apeachScore += (10 - i);
                }
            }

            if (ryanScore > apeachScore) {
                const diff = ryanScore - apeachScore;
                if (diff > maxDiff) {
                    maxDiff = diff;
                    answer = finalRyanShots;
                } else if (diff === maxDiff) {
                    for (let i = 10; i >= 0; i--) {
                        if (finalRyanShots[i] > answer[i]) {
                            answer = finalRyanShots;
                            break;
                        }
                        if (finalRyanShots[i] < answer[i]) {
                            break;
                        }
                    }
                }
            }
            return;
        }

        const arrowsToWin = info[index] + 1;
        if (leftArrows >= arrowsToWin) {
            const newRyanShots = [...ryanShots];
            newRyanShots[index] = arrowsToWin;

            dfs(index + 1, leftArrows - arrowsToWin, newRyanShots);
        }

        dfs(index + 1, leftArrows, ryanShots);
    }
    
    dfs(0, n, new Array(11).fill(0));
    
    return answer;
}