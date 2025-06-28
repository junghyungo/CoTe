function solution(rsp) {
    const jokbo = {
        '2':'0',
        '0':'5',
        '5':'2'
    };
    
    let rsps = rsp.split('');
    let answer = rsps.map(e => jokbo[e]);
    return answer.join('');
}