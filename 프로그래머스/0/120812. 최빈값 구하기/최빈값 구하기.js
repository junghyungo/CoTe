function solution(array) {
  const new_arr = {};
  array.forEach(element => {
    new_arr[element] = new_arr[element] ? new_arr[element]+1 : 1;
  });
  //value가 큰 순서대로 정렬
  const result = Object.keys(new_arr).sort((a, b) => new_arr[b] - new_arr[a]);
  return new_arr[result[0]] === new_arr[result[1]] ? -1 : +result[0];
}