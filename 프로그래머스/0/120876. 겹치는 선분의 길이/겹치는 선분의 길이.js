function solution(lines) {
    const counts = new Array(200).fill(0);
    let result = 0;
    
    lines.forEach(line => {
        const start = line[0] + 100;
        const end = line[1] + 100;
        
        for (let i=start ; i<end ; i++) {
            counts[i] += 1;
        }
    })
    
    counts.forEach(count => {
        if (count > 1) {
            result++;
        }
    })
    
    return result;
}