function solution(my_str, n) {
    const result = [];
    
    let indexA = 0;
    let indexB = n;
    
    while (indexB < my_str.length + 1) {
        result.push(my_str.slice(indexA, indexB));
        indexA = indexB;
        indexB += n;
    }
    
    if (my_str.length % n !== 0) {
        if (indexB > my_str.length) {
            indexB = my_str.length;
            result.push(my_str.slice(indexA, indexB));
        }
    }
    
    return result;
}