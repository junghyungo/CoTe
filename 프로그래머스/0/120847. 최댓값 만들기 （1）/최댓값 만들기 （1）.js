function find_max(arr) {
    let max_value = 0;
    for (let i=0 ; i<arr.length ; i++) {
        if (arr[i] > max_value) {
            max_value = arr[i];
        }
    }
    return max_value;
}

function solution(numbers) {
    let a = find_max(numbers);
    let a_index = numbers.indexOf(a);
    let filtered_numbers = numbers.filter((e, i) => i !== a_index);
    let b = find_max(filtered_numbers);
    return a*b;
}