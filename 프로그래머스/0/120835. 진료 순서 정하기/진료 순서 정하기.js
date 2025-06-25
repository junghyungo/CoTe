function solution(emergency) {
    let answer = [];
    const new_emergency = [...emergency].sort((a, b) => b-a);
    
    for (let i=0 ; i<emergency.length ; i++) {
        let index = emergency.indexOf(new_emergency[i]);
        answer[index] = i+1;
    }
    return answer;
}