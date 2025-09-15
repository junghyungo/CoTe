function solution(users, emoticons) {
    let answer = [0, 0];
    
    const calculate_result = (discounts) => {
        let emtiple_sales = 0;
        let emoticon_sales = 0;
        
        users.forEach(user => {
            let user_purchase_won = 0;

            emoticons.forEach((emoticon_price, i) => {
                const discount_rate = 1 - discounts[i] / 100;

                if (discounts[i] >= user[0]) {
                    user_purchase_won += emoticon_price * discount_rate;
                }
            });
            
            if (user_purchase_won >= user[1]) {
                emtiple_sales += 1;
            } else {
                emoticon_sales += user_purchase_won;
            }
        });
        
        console.log(emtiple_sales, emoticon_sales);
        return [emtiple_sales, emoticon_sales];
    }
    
    const dfs = (index, discounts) => {
        if (index === emoticons.length) {
            const [emtiple, emoticon] =  calculate_result(discounts);
            
            if (emtiple > answer[0]) {
                answer = [emtiple, emoticon];
            } else if (emtiple === answer[0]) {
                if (emoticon > answer[1]) {
                    answer[1] = emoticon;
                }
            }
            
            return;
        }
        
        for (let discount = 10 ; discount <= 40 ; discount += 10) {
            discounts[index] = discount;
            dfs(index + 1, discounts);
        }
    }
    
    dfs(0, new Array(emoticons.length).fill(0));
    
    return answer;
}