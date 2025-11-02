function solution(coin, cards) {
    const n = cards.length;
    const target = n + 1;
    let round = 1;
    
    const hand = new Set(cards.slice(0, n/3));
    const deck = cards.slice(n/3);
    const pending = new Set();
    
    let index = 0;
    
    while (index < deck.length) {
        if (index+2 > deck.length) {
            break;
        }
        
        pending.add(deck[index]);
        pending.add(deck[index+1]);
        index += 2;
        
        let flag = false;
        
        for (const card of hand) {
            if (hand.has(target - card)) {
                hand.delete(card);
                hand.delete(target - card);
                flag = true;
                break;
            }
        }
        
        if (flag) {
            round++;
            continue;
        }
        
        if (coin >= 1) {
            for (const card of hand) {
                if (pending.has(target - card)) {
                    hand.delete(card);
                    pending.delete(target - card);
                    coin--;
                    flag = true;
                    break;
                }
            }
        }

        if (flag) {
            round++;
            continue;
        }

        if (coin >= 2) {
            for (const card of pending) {
                if (pending.has(target - card)) {
                    pending.delete(card);
                    pending.delete(target - card);
                    coin -= 2;
                    flag = true;
                    break;
                }
            }
        }
        
        if (flag) {
            round++;
        } else {
            break;
        }
    }
            
    return round;
}