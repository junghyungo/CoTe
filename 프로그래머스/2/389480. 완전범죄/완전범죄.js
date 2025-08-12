function solution(info, n, m) {
    const max_sum_a = info.length * 3;
    
    let dp = new Array(max_sum_a + 1).fill(Infinity);
    dp[0] = 0;
    
    for (const [a, b] of info) {
        const next_dp = new Array(max_sum_a + 1).fill(Infinity);
        
        for (let sum_a=0 ; sum_a<max_sum_a ; sum_a++) {
            if (dp[sum_a] === Infinity)
                continue;
            
            const a_still = sum_a + a;
            if (a_still < n) {
                if (dp[sum_a] < m) {
                    next_dp[a_still] = Math.min(next_dp[a_still], dp[sum_a]);
                }
            }
            
            const b_still = dp[sum_a] + b;
            if (b_still < m) {
                if (sum_a < n) {
                    next_dp[sum_a] = Math.min(next_dp[sum_a], b_still);
                }
            }
        }
        
        dp = next_dp;
    }
    
    for (let sum_a=0 ; sum_a<=max_sum_a ; sum_a++) {
        if (dp[sum_a] !== Infinity) {
            return sum_a;
        }
    }
    
    return -1;
}