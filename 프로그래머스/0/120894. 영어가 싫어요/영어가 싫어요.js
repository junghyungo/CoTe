function solution(numbers) {
  let numArr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
  numArr.forEach((str, idx) => {
    numbers = numbers.replaceAll(str, idx);
  });
  return Number(numbers);
}
