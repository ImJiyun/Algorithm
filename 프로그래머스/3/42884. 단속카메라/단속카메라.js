function solution(routes) {
    routes.sort((a, b) => a[1] - b[1]);
    
    let cameraCnt = 1;
    let cameraLoc = routes[0][1];
    
    for (let i = 1; i < routes.length; i++) {
        const next = routes[i][0]; 
        if (next > cameraLoc) {
            cameraLoc = routes[i][1];
            cameraCnt++;
        }
    }
    
    return cameraCnt;
}