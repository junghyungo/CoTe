

function solution(my_string) {
    let numbers = [];
    
    for (let i=0 ; i<my_string.length ; i++) {
        let num = parseInt(my_string[i]);
        if (isNaN(num) === false) {
            numbers.push(num)
        }
    }
    
    let sum = 0;
    for (let i=0 ; i<numbers.length ; i++) {
        sum += numbers[i];
    }
    
    return sum;
}
