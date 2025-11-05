function solution(n, k) {
    let result = 0;
    const kJinsu = n.toString(k);
    const numbers = kJinsu.split('0');
    
    const isSosu = (n) => {    
        for (let i=2 ; i<=Math.sqrt(n) ; i++) {
            if (n%i === 0) {
                return false;
            }
        }
        return true;
    }
    
    for (num of numbers) {
        const n = Number(num);
        if (n === 1 || n === 0) {
            continue;
        }
        if (isSosu(n)) {
            result++;
        }
    }
    
    return result;
}