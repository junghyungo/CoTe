const fs = require('fs');
const filePath = '/dev/stdin';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = Number(input[0]);
const words = input.slice(1);

let len = 0;
let answer;

for (let i=0 ; i<N ; i++) {
  for (let j=i+1 ; j<N ; j++) {
    const a = words[i];
    const b = words[j];

    let current_len = 0;
      
    for (let k=0 ; k<Math.min(a.length, b.length); k++) {
      if (a[k] !== b[k]) break;
      current_len = k + 1;
    }

    if (len < current_len) {
      len = current_len;
      answer = [a, b];
    }
  }
}

console.log(answer[0]);
console.log(answer[1]);