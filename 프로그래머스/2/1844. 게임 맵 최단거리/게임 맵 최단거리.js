function solution(maps) {
    const dir = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    const n = maps.length;
    const m = maps[0].length;
    
    let x = 0;
    let y = 0;
    
    const queue = [[x, y]];
    const visited = new Set();
    
    while (queue.length > 0) {
        [x, y] = queue.shift();
        if (x === n - 1 && y === m - 1) return maps[n-1][m-1];
        visited.add(`${x},${y}`)
        
        for (let [r, c] of dir) {
            let nr = x + r;
            let nc = y + c;
            if (nr < 0 || nc < 0 || nr > n - 1 || nc > m - 1) continue;
            if (maps[nr][nc] === 1 && !visited.has(`${nr},${nc}`)) {
                maps[nr][nc] += maps[x][y];
                queue.push([nr, nc])
            }
        }
    }
    
    return -1;
}