function solution(today, terms, privacies) {
    const answer = [];
    
    const termsMap = new Map();
    terms.forEach((term) => {
        termsMap.set(term.split(' ')[0], term.split(' ')[1]);
    });
    
    const dateToNumber = (date) => {
        let dateNum = 0;
        dateNum += parseInt(date[0]) * 12 * 28;
        dateNum += parseInt(date[1]) * 28;
        dateNum += parseInt(date[2]);
        return dateNum;
    };
    
    const todayNum = dateToNumber(today.split('.'));
    
    privacies.forEach((privacy, index) => {
        let dateNum = dateToNumber(privacy.substring(0, 10).split('.'));
        dateNum += termsMap.get(privacy[11]) * 28;

        if (dateNum <= todayNum) {
            answer.push(index + 1);
        }
    });
    
    return answer;
}