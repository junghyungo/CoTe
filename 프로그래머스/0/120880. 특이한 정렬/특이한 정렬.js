function solution(numlist, n) {
    const result = [];
    const temp = [];
    
    for (let i=0 ; i<numlist.length ; i++) {
        temp[i] = [Math.abs(numlist[i] - n), numlist[i]];
    }
    
    temp.sort((a, b) => b[1] - a[1]);
    temp.sort((a, b) => a[0] - b[0]);
    
    for (let i=0 ; i<temp.length ; i++) {
        result[i] = temp[i][1];
    }
    
    return result;
}