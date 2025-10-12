function calculate(expression) {
    let result = 0;
    let cal = true;
    let flag = false;
    let returnVal = '';
    
    expression.split(' ').forEach(n => {
        if (!isNaN(n)) {
            if (flag) {
                if (result == n) {
                    returnVal = 'O';
                } else {
                    returnVal = 'X';
                }
            } else {
                if (cal) {
                    result += Number(n);
                } else {
                    result -= Number(n);
                }   
            }
        } else {
            if (n === '+') {
                cal = true;
            } else if (n === '-') {
                cal = false;
            } else if (n === '=') {
                flag = true;
            }
        }
    })
    
    return returnVal;
}

function solution(quiz) {
    const answer = [];
    quiz.forEach((q) => {
        answer.push(calculate(q));
    })
    return answer;
}