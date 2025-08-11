function solution(n, w, num) {
    const num_y = Math.floor((num-1) / w);
    const num_x = (num_y%2 === 0) ? (num-1)%w : w-1-((num-1)%w);
    
    let cnt = 0;
    const height = Math.ceil(n/w);
    
    for (let y=num_y ; y<height ; y++) {
        const idx = (y%2 === 0) ? num_x : w-1-num_x;
        const boxes = y*w + idx + 1;
        
        if (boxes <= n) cnt++;
    }
    
    return cnt;
}