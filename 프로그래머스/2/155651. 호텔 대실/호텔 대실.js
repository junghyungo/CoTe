function change_to_minute(time) {
    let [hour, minute] = time.split(':');
    return parseInt(hour)*60 + parseInt(minute);
}

function solution(book_time) {
    let rooms = [];
    let book_time_minute = [];
    
    for (let i=0 ; i<book_time.length ; i++) {
        book_time_minute[i] = [
            change_to_minute(book_time[i][0]),
            change_to_minute(book_time[i][1])
        ]
    }
    
    book_time_minute.sort((a,b) => { return a[0]-b[0]; })
    book_time_minute.forEach(time => {
        if (rooms.length === 0) {
            rooms.push(time[1] + 10)
        } else {
            let hasSonNim = false;
            
            rooms.sort((a,b) => a-b);
            for (let i=0 ; i<rooms.length ; i++) {
                if (rooms[i] <= time[0]) {
                    rooms[i] = time[1] + 10;
                    hasSonNim = true;
                    break;
                }
            }
            
            if (!hasSonNim) {
                rooms.push(time[1] + 10);
            }
        }
    })
    
    return rooms.length;
}