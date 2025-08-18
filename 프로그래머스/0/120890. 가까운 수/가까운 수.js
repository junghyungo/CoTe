function solution(array, n) {
    array.sort((a, b) => a - b);
    
    let answer = 0;
    let minDiff = Infinity;
    
    for (const num of array) {
        const diff = Math.abs(num - n);

        if (diff < minDiff) {
            minDiff = diff;
            answer = num;
        }
    }
    
    return answer;
}