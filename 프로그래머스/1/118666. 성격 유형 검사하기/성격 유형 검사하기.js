function solution(survey, choices) {
    let result = '';
    
    let scores = new Map();
    
    const VARIANTS = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N'];
    VARIANTS.forEach((v) => {
       scores.set(v, 0); 
    });
    
    survey.forEach((s, index) => {
        const c = choices[index];
        
        if (c < 4) {
            const current = scores.get(s[0]);
            scores.set(s[0], current + 4 - c);
            // console.log(s, c, s[0], scores.get(s[0]));
        } else if (c > 4) {
            const current = scores.get(s[1]);
            scores.set(s[1], current + c - 4);
            // console.log(s, c, s[1], scores.get(s[1]));
        }
    });
    
    for (let i=0 ; i<VARIANTS.length ; i+=2) {
        if(scores.get(VARIANTS[i]) >= scores.get(VARIANTS[i+1])) {
            result += VARIANTS[i];
        } else {
            result += VARIANTS[i+1];
        }
    }
    
    return result;
}