function solution(n) {
    let result = 0;
    
    n.toString().split('').forEach((num) => {
        result += Number(num);
    })
    
    return result;
}