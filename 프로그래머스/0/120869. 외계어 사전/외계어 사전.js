function solution(spell, dic) {
    let answer = 2;
    
    dic.forEach(d => {
        let flag = 0;
        spell.forEach(s => {
            if (d.indexOf(s) !== -1) {
                flag++;
            }
        })
        
        if (flag === spell.length) {
            answer = 1;
            return;
        }
    })
    
    return answer;
}