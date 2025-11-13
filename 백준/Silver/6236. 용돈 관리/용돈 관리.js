const fs = require('fs');
const filePath = '/dev/stdin';
const input = fs.readFileSync(filePath).toString().trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);
const wons = input.slice(1).map(Number);

function inchulCount(k) {
    let count = 1;
    let currentMoney = k;

    for (const won of wons) {
        if (currentMoney < won) {
            count++;
            currentMoney = k;
        }    
        currentMoney -= won;
    }
    
    return count;
}

let low = Math.max(...wons);
let high = wons.reduce((acc, val) => acc + val, 0);

let answer = high;

while (low <= high) {
    const mid = Math.floor((low+high) / 2);

    const count = inchulCount(mid);

    if (count <= M) {
        answer = mid;
        high = mid - 1;
    } else {
        low = mid + 1;
    }
}

console.log(answer);