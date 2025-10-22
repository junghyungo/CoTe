function solution(score) {
    const len = score.length;
    const result = [];
    const avg_original = [];
    
    for (let i=0 ; i<len ; i++) {
        avg_original[i] = (score[i][0] + score[i][1]) / 2;
    }
    
    const avg_sorted = [...avg_original].sort((a, b) => b - a);
    
    avg_original.forEach(avg => {
        result.push(avg_sorted.indexOf(avg) + 1);
    })
    
    return result;
}