function solution(n) {
    let sum = 0;
    const str_n = n.toString();
    
    for (let i=0 ; i<str_n.length ; i++) {
        sum += Number(str_n[i]);
    }
    
    return sum;
}