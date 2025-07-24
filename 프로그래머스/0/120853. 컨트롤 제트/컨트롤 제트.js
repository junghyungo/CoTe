function solution(s) {
    const arr = s.split(' ');
    let answer = 0;
    
    arr.forEach((num, i) => {
        if (num === 'Z') {
            answer -= Number(arr[i-1]);
        } else {
            answer += Number(num);
        }
    });
    
    return answer;
}