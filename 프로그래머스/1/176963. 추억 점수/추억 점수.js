function cal(name, yearning, photo, map) {
    let new_names = photo.filter(it => name.includes(it));
    
    let score = 0;
    new_names.forEach(new_name => score += map.get(new_name));
    
    return score;
}

function solution(name, yearning, photo) {
    let name_map = new Map();
    for (let i=0 ; i<name.length ; i++) {
        name_map.set(name[i], yearning[i]);
    }
    
    let result = [];
    for (let i=0 ; i<photo.length ; i++) {
        result[i] = cal(name, yearning, photo[i], name_map);
    }
    
    
    return result;
}