function solution(fees, records) {
    
    // 시간 -> 분
    const time_to_minute = (time) => {
        const [h, m] = time.split(':');
        return Number(h)*60 + Number(m);
    }
    
    const total_time = new Map();
    const parking_lot = new Map();
    
    // 1. 입출 기록
    records.forEach((r) => {
        const [time, car_num, type] = r.split(' ');
        const minute = time_to_minute(time);
        
        if (type === 'IN') {
            parking_lot.set(car_num, minute);
        } else {
            const in_time = parking_lot.get(car_num);
            const parking_time = minute - in_time;
            const current_total = total_time.get(car_num) || 0;
            
            total_time.set(car_num, current_total + parking_time);
            parking_lot.delete(car_num);
        }
    });
    
    // 2. 출차 기록이 없는 차량 처리
    const last_time = time_to_minute('23:59');
    for (const [car_num, in_time] of parking_lot.entries()) {
        const parking_time = last_time - in_time;
        const current_total = total_time.get(car_num) || 0;
        total_time.set(car_num, current_total + parking_time);
    }

    // 3. 요금 계산 및 정렬
    const [base_time, base_fee, unit_time, unit_fee] = fees;
    const sorted_car_nums = [...total_time.keys()].sort();
    
    const answer = sorted_car_nums.map((car_num) => {
        const time = total_time.get(car_num);
        
        if (time <= base_time) {
            return base_fee;
        }
        
        const extra_time = time - base_time;
        const extra_fee = Math.ceil(extra_time / unit_time) * unit_fee;
        
        return base_fee + extra_fee;
    });

    return answer;
}