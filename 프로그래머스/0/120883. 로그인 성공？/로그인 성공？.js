function solution(id_pw, db) {
    let status = 0;
    let id = -1;
    const result = ['fail', 'wrong pw', 'login'];
    
    for (let i=0 ; i<db.length ; i++) {
        if (db[i][0] === id_pw[0]) {
            status = 1;
            id = i;
        }
    }
    
    if (status === 1) {
        if (db[id][1] === id_pw[1]) {
            status = 2;
        }
    }
    
    return result[status];
}