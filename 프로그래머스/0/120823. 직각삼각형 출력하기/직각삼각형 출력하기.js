const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {
    let answer = "";
    
    for (let i=0 ; i<input[0] ; i++) {
        for (let j=0 ; j<=i ; j++) {
            answer += "*";
        }
        answer += "\n";
    }
    
    console.log(answer);
});