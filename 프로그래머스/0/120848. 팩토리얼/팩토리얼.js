function solution(n) {
    let facto = 1;
    for (let i=1 ; i<11 ; i++) {
        facto *= i;
        if (facto > n) {
            return i-1;
        }
        else if (facto === n) {
            return i;
        }
    }
}