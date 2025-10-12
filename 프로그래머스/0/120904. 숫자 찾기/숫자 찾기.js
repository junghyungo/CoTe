function solution(num, k) {
    const index = num.toString().indexOf(k);
    if (index !== -1) {
        return index + 1;
    } else {
        return index;
    }
}