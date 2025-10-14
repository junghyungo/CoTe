function solution(polynomial) {
    let result = '';
    
    let xCount = 0;
    let numCount = 0;
    
    polynomial.split(' ').forEach((p) => {
        if (p.includes('x')) {
            if (p === 'x') {
                xCount++;
            } else {
                xCount += Number(p.slice(0, -1));
            }
        } else if (p !== '+') {
            numCount += Number(p);
        }
    })
    
    if (xCount > 0) {
        if (xCount === 1) {
            result = 'x';
        } else {
            result = xCount.toString() + 'x';
        }
        
        if (numCount > 0) {
            result += ' + ' + numCount.toString();
        }
    } else {
        if (numCount > 0) {
            result = numCount.toString();
        }   
    }
    
    return result;
}