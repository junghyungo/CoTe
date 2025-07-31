function solution(strlist) {
    let result = [];
    
    strlist.forEach((str) => {
       result.push(str.length);
    });
    
    return result;
}