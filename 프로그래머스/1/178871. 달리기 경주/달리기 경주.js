function solution(players, callings) {
    const players_position = {};
  
    for (let i=0 ; i<players.length ; i++) {
        players_position[players[i]] = i;
    }

    for (let i=0 ; i<callings.length ; i++) {
        const idx = players_position[callings[i]];
        const temp = players[idx-1];
      
        players[idx-1] = callings[i];
        players[idx] = temp;
      
        players_position[callings[i]] = idx-1;
        players_position[temp] = idx;
    }
    
    return players;
}