function solution(s) {
    s = s.toLowerCase().split(' ');
    const answer = s.map(word => {
        return (word.charAt(0).toUpperCase() + word.slice(1));
    }).join(' ');
    
    return answer;
}