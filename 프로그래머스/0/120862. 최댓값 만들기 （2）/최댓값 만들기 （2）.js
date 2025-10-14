function solution(numbers) {
    numbers = numbers.sort((a, b) => a - b);
    
    const a = numbers[0] * numbers[1];
    const b = numbers[numbers.length - 1] * numbers[numbers.length - 2];
    
    console.log(a, b)
    
    return Math.max(a, b);
}