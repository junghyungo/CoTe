function solution(s) {
    let totalCount = 0;
    let zeroCount = 0;
    
    while (s.length > 1) {
        const sLength = s.length;
        s = s.split('0').join('');
        console.log(s)
        totalCount++;
        zeroCount += (sLength - s.length);
        s = s.length.toString(2);
    };
    
    return [totalCount, zeroCount];
}