function solution(slice, n) {
    var answer = 0;
    
    if (slice <= n) {
        answer += Math.floor(n/slice)
        if (n%slice != 0) {
            answer++
        }
    } else {
        answer++
    }
    
    return answer;
}