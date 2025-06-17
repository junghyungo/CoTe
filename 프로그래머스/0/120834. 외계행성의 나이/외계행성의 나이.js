function solution(age) {
    const P962 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'];
    const ageArr = String(age).split("");
    let answer = '';
    for (let i=0 ; i<ageArr.length ; i++) {
        answer += P962[Number(ageArr[i])];
    }
    return answer;
}