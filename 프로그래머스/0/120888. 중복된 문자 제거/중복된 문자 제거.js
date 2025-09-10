function solution(my_string) {
  const uniqueCharsSet = new Set(my_string);
  const uniqueCharsArray = [...uniqueCharsSet];
  const result = uniqueCharsArray.join('');

  return result;
}