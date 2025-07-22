function solution(n) {
    let soinsu = new Set();
    
    for (let i=2 ; i<n+1 ; i++) {
        while (n % i === 0) {
            soinsu.add(i);
            n /= i;
        }
    }
    
    return [...soinsu];
}