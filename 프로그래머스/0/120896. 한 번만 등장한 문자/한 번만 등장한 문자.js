function solution(s) {
    const uniqueChars = [...new Set(s)].sort();

    const counts = uniqueChars.map(char => {
        let count = 0;
        for (let i = 0; i < s.length; i++) {
            if (s[i] === char) {
                count++;
            }
        }
        return count;
    });

    const result = uniqueChars.filter((char, index) => counts[index] === 1);
    return result.join('');
}