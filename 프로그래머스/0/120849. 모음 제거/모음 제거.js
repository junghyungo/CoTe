const moum = ['a', 'e', 'i', 'o', 'u'];

function replace_char(string, char) {
    return string.replaceAll(char, '');
}

function solution(my_string) {
    for (let i=0 ; i<moum.length ; i++) {
        my_string = replace_char(my_string, moum[i]);
    }
    return my_string;
}