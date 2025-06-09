function stringReverse(original_string) {
    let new_string = "";
    
    for (let i=original_string.length-1 ; i>=0 ; i--) {
        new_string += original_string[i];
    }
    
    return new_string;
}

function solution(my_string) {
    return stringReverse(my_string);
}