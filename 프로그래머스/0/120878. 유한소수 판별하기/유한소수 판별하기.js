function solution(a, b) {
    const maxGongYakSu = (j, m) => {
        while (m !== 0) {
            let temp = m;
            m = j % m;
            j = temp;
        }
        return j;
    }
    
    let bunmo = b / maxGongYakSu(a, b);
    
    while (bunmo % 2 === 0) {
        console.log('asdf')
        bunmo /= 2;
    }
    while (bunmo % 5 === 0) {
        bunmo /= 5;
    }
    
    if (bunmo === 1) {
        return 1;
    } else {
        return 2;
    }
}