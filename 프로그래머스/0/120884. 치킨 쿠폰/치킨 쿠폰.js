function solution(chicken) {
    let coupon = chicken;
    let result = 0;
    
    while(coupon > 9) {
        result += Math.floor(coupon / 10);
        coupon = Math.floor((coupon/10) + (coupon%10));
    }
    
    return result;
}