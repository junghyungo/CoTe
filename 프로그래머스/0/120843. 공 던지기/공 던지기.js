function solution(numbers, k) {
    let idx = 0;
    for (let i=1 ; i<k ; i++) {
        idx += 2;
    }
    return numbers[idx%numbers.length];
}