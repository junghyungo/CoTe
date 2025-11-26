const fs = require('fs');
const filePath = '/dev/stdin';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const [N, M] = input[0].split(' ').map(Number);
const bosuks = input.slice(1).map(Number);

let start = 1;
let end = Math.max(...bosuks);

let answer = 0;

while (start <= end) {
    let sum = 0;
    let mid = Math.floor((start + end) / 2);
    
    bosuks.forEach(bosuk => {
        sum += Math.ceil(bosuk/mid);
    })

    if (sum <= N) {
        answer = mid;
        end = mid - 1;
    } else {
        start = mid + 1;
    }
}

console.log(answer)
