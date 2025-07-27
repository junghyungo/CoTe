function convert_sec(time) {
  const [m, s] = time.split(':');
  return Number(m)*60 + Number(s);
}

function convert_min(time) {
  const h = Math.floor(time / 60) + "";
  const m = (time % 60) + "";
  return `${h.padStart(2, "0")}:${m.padStart(2, "0")}`;
}

function check_is_opening(current, start, end) {
    if ((start <= current) && (current < end)) {
        return end;
    } else {
        return current;
    }
}

function solution(video_len, pos, op_start, op_end, commands) {
    const video_sec = convert_sec(video_len);
    const open_start_sec = convert_sec(op_start);
    const open_end_sec = convert_sec(op_end);
    
    let current_sec = convert_sec(pos);
    
    for (let i=0 ; i<commands.length ; i++) {
        current_sec = check_is_opening(current_sec, open_start_sec, open_end_sec);
        
        if (commands[i] === 'next') {
            current_sec += 10;
            if (current_sec > video_sec) {
                current_sec = video_sec;
            }
        } else {
            current_sec -= 10;
            if (current_sec < 0) {
                current_sec = 0;
            }
        }
        
        current_sec = check_is_opening(current_sec, open_start_sec, open_end_sec);
    }
    
    return convert_min(current_sec);
}