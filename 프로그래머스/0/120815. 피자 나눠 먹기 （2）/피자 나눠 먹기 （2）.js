function solution(n) {
    let lcm = 1;
    
    if (n%6 == 0)
        return n/6
    
    while (true) {
        if ((lcm%n == 0) && (lcm%6 == 0))
            break
        lcm++
    }
    
    return lcm/6;
}