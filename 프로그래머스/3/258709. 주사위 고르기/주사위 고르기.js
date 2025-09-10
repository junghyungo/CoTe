function solution(dice) { 
    const dice_count = dice.length;
    const dices = new Array(dice_count).fill(0).map((_, idx) => idx+1);
    
    const check_sum = (n, arr, s, res) => {
        if (n === arr.length) {
            res.push(s);
            return;
        }
        for (let i=0 ; i<dice[arr[n]].length ; i++) {
            check_sum(n+1, arr, s+dice[arr[n]][i], res);
        }
    }
    
    let sum = [];
    const choose_dice = (num, a_dice, k) => {
        if (num === dice.length/2) {
            sum.push(a_dice);
            return;
        }
        for (let i=k+1 ; i<dice.length ; i++) {
            choose_dice(num+1, [...a_dice, i], i);
        }
    }
    
    for (let i=0 ; i<dice.length ; i++) {
        choose_dice(1, [i], i);
    }
    
    const binary_search = (num, arr) => {
        let left = 0;
        let right = arr.length - 1;
        
        if (num > arr[right])
            return right+1;
        
        while (left < right) {
            let mid = ~~((left + right) / 2);
            if (arr[mid] < num)
                left = mid + 1;
            else
                right = mid;
        }
        
        return left;
    }
    
    let max;
    let max_win = 0;
    
    for (let i=0 ; i<sum.length/2 ; i++) {
        let a_res = [];
        let b_res = [];
        check_sum(0, sum[i], 0, a_res);
        check_sum(0, sum[sum.length-1-i], 0, b_res);
        
        let a_c = 0;
        let b_c = 0;
        a_res.sort((a, b) => a - b);
        b_res.sort((a, b) => a - b);
        
        for (let j=0 ; j<a_res.length ; j++) {
            let temp = binary_search(a_res[j], b_res);
            a_c += temp;
        }
        for (let j=0 ; j<b_res.length ; j++) {
            let temp = binary_search(b_res[j], a_res);
            b_c += temp;
        }
        
        if (a_c > b_c && a_c > max_win) {
            max = sum[i];
            max_win = a_c;
        } else if (b_c > max_win) {
            max = sum[sum.length - 1 - i];
            max_win = b_c;
        }
    }
    
    return max.map((a) => a+1);
}