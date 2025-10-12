function solution(s1, s2) {
    const intersection = s1.filter(element => s2.includes(element));
    return intersection.length;
}