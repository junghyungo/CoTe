function solution(friends, gifts) {
    const gifting = [];
    const giftIndex = [];
    let nextGift = [];
    
    // 배열 초기화
    for (const giver of friends) {
        gifting[giver] = [];
        giftIndex[giver] = 0;
        nextGift[giver] = 0;

        for (const receiver of friends) {
            gifting[giver][receiver] = 0;
        }
    }
    
    // 선물 주고받기
    for (const gift of gifts) {
        const [giver, receiver] = gift.split(' ');
        gifting[giver][receiver] += 1;
        giftIndex[giver] += 1;
        giftIndex[receiver] -= 1;
    }

    // 주고받은 선물 계산
    for (let i=0 ; i<friends.length ; i++) {
        const a = friends[i];
        for (let j=i+1 ; j<friends.length ; j++) {
            const b = friends[j];

            // 같으면 지수 비교
            if (gifting[a][b] === gifting[b][a]) {
                if (giftIndex[a] > giftIndex[b]) {
                    nextGift[a] += 1;
                } else if (giftIndex[a] < giftIndex[b]) {
                    nextGift[b] += 1;
                }
            } else {
                if (gifting[a][b] > gifting[b][a]) {
                    nextGift[a] += 1;
                } else {
                    nextGift[b] += 1;
                }
            }
        }
    }
    
    return Math.max(...Object.values(nextGift));
}