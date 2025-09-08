function solution(edges) {
    const answer = [0, 0, 0, 0];
    const nodeMap = new Map();
    
    edges.forEach(([from, to]) => {
        if (!nodeMap.has(from))
            nodeMap.set(from, { send: 0, receive: 0 });
        
        if (!nodeMap.has(to))
            nodeMap.set(to, { send: 0, receive: 0 });
        
        nodeMap.get(from).send++;
        nodeMap.get(to).receive++;
    })
    
    let totalGraphs = 0;
    for (const [node, counts] of nodeMap.entries()) {
        if (counts.send >= 2 && counts.receive === 0) {
            answer[0] = node;
            totalGraphs = counts.send;
            break;
        }
    }
    
    for (const [node, counts] of nodeMap.entries()) {
        if (node === answer[0])
            
            continue;
        if (counts.send === 0) {
            answer[2]++;
        } else if (counts.send >= 2 && counts.receive >= 2) {
            answer[3]++;
        }
    }
    
    answer[1] = totalGraphs - answer[2] - answer[3];
    
    return answer;
}