function solution(my_string) {
    let numbers = [];
    
    for (let i=0 ; i<my_string.length ; i++) {
        let num = parseInt(my_string[i]);
        
        if (isNaN(num) === false) {
            numbers.push(num);
        }
    }
    
    return numbers.sort();
}