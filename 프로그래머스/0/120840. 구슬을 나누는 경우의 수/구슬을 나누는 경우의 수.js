const factor = (num) => (num === 0 ? 1 : num * factor(num-1));

function solution(balls, share) {
    return Math.round(
        factor(balls) / (factor(balls-share) * factor(share))
    );
}