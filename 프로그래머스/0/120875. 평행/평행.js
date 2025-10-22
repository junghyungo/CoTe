function solution(dots) {
    const getGradient = (a, b) => {
        return Math.abs(a[0] - b[0]) / Math.abs(a[1] - b[1]);
    }
    
    if (getGradient(dots[0], dots[1]) === getGradient(dots[2], dots[3])) {
        return 1;
    }
    if (getGradient(dots[0], dots[2]) === getGradient(dots[1], dots[3])) {
        return 1;
    }
    if (getGradient(dots[0], dots[3]) === getGradient(dots[1], dots[2])) {
        return 1;
    }
    
    return 0;
}