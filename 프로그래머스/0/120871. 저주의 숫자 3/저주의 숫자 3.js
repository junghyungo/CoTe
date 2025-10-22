function solution(n) {
    let flag = 0;
    
    for (let i=0 ; i<n+flag ; i++) {
        if (String(i).indexOf(3) !== -1 || i%3 === 0) {
            flag++;
        }
    }
    
    return n + flag - 1;
}