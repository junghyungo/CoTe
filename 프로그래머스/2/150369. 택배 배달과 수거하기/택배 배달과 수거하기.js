function solution(cap, n, deliveries, pickups) {
    let answer = 0;

    let pending_d = 0;
    let pending_p = 0;

    for (let i=n-1 ; i>=0 ; i--) {
        pending_d += deliveries[i];
        pending_p += pickups[i];

        while (pending_d > 0 || pending_p > 0) {
            answer += (i+1)*2;
            pending_d -= cap;
            pending_p -= cap;
        }
    }

    return answer;
}