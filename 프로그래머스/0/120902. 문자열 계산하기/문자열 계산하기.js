function solution(my_string) {
    let result = 0;
    let cal = true;
    
    my_string.split(' ').forEach(n => {
        if (Number(n)) {
            if (cal) {
                result += Number(n);    
            } else {
                result -= Number(n);   
            }
        } else {
            if (n === '+') {
                cal = true;
            } else {
                cal = false;
            }
        }
    })
    
    return result;
}