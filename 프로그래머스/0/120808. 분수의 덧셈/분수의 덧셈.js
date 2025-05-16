function cal_gcd(a, b) {
    return (a%b === 0) ? b : cal_gcd(b, a%b)
}

function solution(numer1, denom1, numer2, denom2) {
    let numerator = (numer1 * denom2) + (numer2 * denom1);
    let denominator = denom1 * denom2;
    let gcd = cal_gcd(numerator, denominator);
    
    // 최대공약수를 분자, 분모에 나누고 배열에 넣기
    return [numerator/gcd, denominator/gcd]
}