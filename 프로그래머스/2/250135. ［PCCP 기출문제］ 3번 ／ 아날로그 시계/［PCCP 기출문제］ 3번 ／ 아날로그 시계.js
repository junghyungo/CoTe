function solution(h1, m1, s1, h2, m2, s2) {
    const SECONDS_ANGLE = 360 / 60;
    const MINUTES_ANGLE = 360 / 60 / 60;
    const HOURS_ANGLE = 360 / 12 / 60 / 60;

    let cnt = 0;

    let start_time = h1 * 60 * 60 + m1 * 60 + s1;
    let end_time = h2 * 60 * 60 + m2 * 60 + s2;

    const start_hour_angle = (start_time * HOURS_ANGLE) % 360;
    const start_minute_angle = (start_time * MINUTES_ANGLE) % 360;
    const start_seconds_angle = (start_time * SECONDS_ANGLE) % 360;

    // 시작 시간에 초침과 시침이 겹쳐있으면 카운트
    if (start_seconds_angle === start_hour_angle) cnt++;
    // 시작 시간에 초침과 분침이 겹쳐있으면 카운트
    if (start_seconds_angle === start_minute_angle) cnt++;
    // 시작 시간에 시침, 분침, 초침 3가지가 겹쳐있는 경우 -1
    if (start_seconds_angle === start_hour_angle && 
        start_seconds_angle === start_minute_angle) cnt--;

    // 1초마다 겹쳤는지 확인
    // 현재 초침의 각도가 시침, 분침 각도보다 작다가 1초 뒤에 크거나 같으면 겹쳐진 것
    while (start_time < end_time) {
        //현재 시간 시침, 분침, 초침 각도
        const current_hours_angle = (start_time * HOURS_ANGLE) % 360;
        const current_minutes_angle = (start_time * MINUTES_ANGLE) % 360;
        const current_seconds_angle = (start_time * SECONDS_ANGLE) % 360;

        const next_time = start_time + 1;

        // 1초 뒤 시침, 분침, 초침 각도
        // 360도일 때 모듈러 연산을 하면 0이 되므로 0일 경우에는 360으로 설정해줌
        const next_hours_angle = (next_time * HOURS_ANGLE) % 360 || 360;
        const next_minutes_angle = (next_time * MINUTES_ANGLE) % 360 || 360;
        const next_seconds_angle = (next_time * SECONDS_ANGLE) % 360 || 360;

        // 초침이 시침 뒤에 있었는데 1초 뒤에 시침 앞으로 가면 카운트+1
        if (current_seconds_angle < current_hours_angle &&
            next_seconds_angle >= next_hours_angle) cnt++;
        // 초침이 분침 뒤에 있었는데 1초 뒤에 분침 앞으로 가면 카운트+1
        if (current_seconds_angle < current_minutes_angle &&
            next_seconds_angle >= next_minutes_angle) cnt++;
        // 1초 뒤에 시침 분침 초침 3개가 겹치면 -1(0시, 12시)
        if (next_seconds_angle === next_hours_angle &&
            next_seconds_angle === next_minutes_angle) cnt--;

        // 시작 시간 업데이트
        start_time = next_time;
    }

    return cnt;
}