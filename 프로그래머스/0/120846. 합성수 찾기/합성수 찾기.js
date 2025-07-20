function solution(n) {
    if (n < 4) {
        return 0;
    }
    
    let answer = 0;
    
    for (let i=1 ; i<n+1 ; i++) {
        let count = 0;
        
        for (let j=1 ; j<i+1 ; j++) {
            if (i % j === 0) {
                count += 1;
            }
        }
        
        if (count >= 3) {
            console.log(i)
            answer += 1;
        }
    }
    
    return answer;
}