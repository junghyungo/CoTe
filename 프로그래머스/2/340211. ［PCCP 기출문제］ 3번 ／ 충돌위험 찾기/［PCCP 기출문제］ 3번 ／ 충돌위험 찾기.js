
function solution(points, routes) {
    const robotPaths = [];
    
    for (let i=0 ; i<routes.length ; i++) {
        const path = [];
        const route = routes[i];
        
        for (let j=0 ; j<route.length-1 ; j++) {
            const startPoint = points[route[j] - 1];
            const endPoint = points[route[j+1] - 1];
            
            const shortestPath = getShortestPath(startPoint, endPoint);
            
            if (j > 0) { shortestPath.shift(); }
            
            path.push(...shortestPath);
        }
        
        robotPaths.push(path);
    }
    
    let collisionCount = 0;
    const maxTime = Math.max(...robotPaths.map(path => path.length));
    
    for (let time=0 ; time<maxTime ; time++) {
        const positionMap = new Map();
        
        for (let robot=0 ; robot<robotPaths.length ; robot++) {
            if (time < robotPaths[robot].length) {
                const position = robotPaths[robot][time];
                const posKey = `${position[0]},${position[1]}`;
                
                if (!positionMap.has(posKey)) {
                    positionMap.set(posKey, []);
                }
                positionMap.get(posKey).push(robot);
            }
        }
        
        for (const [position, robots] of positionMap) {
            if (robots.length > 1) {
                collisionCount++;
            }
        }
    }
    
    return collisionCount;
}

function getShortestPath(start, end) {
    const path = [];
    let [currentR, currentC] = start;
    const [targetR, targetC] = end;
    
    path.push([currentR, currentC]);
    
    while (currentR !== targetR) {
        if (currentR < targetR) { currentR++; }
        else { currentR--; }
        path.push([currentR, currentC]);
    }
    
    while (currentC !== targetC) {
        if (currentC < targetC) { currentC++; }
        else { currentC--; }
        path.push([currentR, currentC]);
    }
    
    return path;
}