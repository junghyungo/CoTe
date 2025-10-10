function solution(queue1, queue2) {
    const sum_of = (arr) => arr.reduce((a, c) => a + c, 0);
    
    let sum1 = sum_of(queue1);
    let sum2 = sum_of(queue2);
    const totalSum = (sum1 + sum2);
    const goal = totalSum / 2;
    
    if (totalSum % 2 !== 0) return -1;
    
    const totalQueue = [...queue1, ...queue2];
    const maxCount = totalQueue.length * 2;
    let p1 = 0;
    let p2 = queue1.length;
    
    for (let count=0 ; count<maxCount ; count++) {
        if (sum1 === goal) {
            return count;
        }
        
        if (sum1 > goal) {
            sum1 -= totalQueue[p1];
            p1++;
            // console.log(p1, p2, sum1, sum2);
        } else if (sum1 < goal) {
            sum1 += totalQueue[p2];
            p2++;
            // console.log(p1, p2, sum1, sum2);
        }
    }
    
    return -1;
}