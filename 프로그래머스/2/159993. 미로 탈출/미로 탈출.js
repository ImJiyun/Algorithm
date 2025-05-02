function solution(maps) {
    let traces = Array.from({ length: maps.length }, () => Array(maps[0].length).fill(0));

    const N = maps.length;
    const M = maps[0].length;
    let visited = new Set();
    let exitR;
    let exitC;
    const dir = [[-1, 0], [1, 0], [0, 1], [0, -1]];
    
    let queue = [];
    let found = false;
    
    for (let r = 0; r < N; r++) {
        for (let c = 0; c < M; c++) {
            if (maps[r][c] === 'S') {
                visited.add(`${r},${c}`);
                queue.push([r,c]);
            } else if (maps[r][c] === 'E') {
                exitR = r;
                exitC = c;
            }
        }
    }
    
    while (queue.length > 0) {
        const [r, c] = queue.shift();
        
        if (maps[r][c] === 'L') {
            queue = [[r,c]];
            found = true;
            break;
        }
        
        for (let [dr, dc] of dir) {
            const nr = dr + r;
            const nc = dc + c;
            if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
            if (visited.has(`${nr},${nc}`)) continue;
            if (maps[nr][nc] === 'X') continue;
            traces[nr][nc] = traces[r][c] + 1;
            visited.add(`${nr},${nc}`);
            queue.push([nr, nc]);
        }
        
    }
    
    if (!found) return -1;
    found = false;
    
    visited = new Set();
    while (queue.length > 0) {
        const [r, c] = queue.shift();
        visited.add(`${r},${c}`);
        
        if (maps[r][c] === 'E') {
            found = true;
            break;
        }
        
        for (let [dr, dc] of dir) {
            const nr = dr + r;
            const nc = dc + c;
            if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
            if (visited.has(`${nr},${nc}`)) continue;
            if (maps[nr][nc] === 'X') continue;
            traces[nr][nc] = traces[r][c] + 1;
            visited.add(`${nr},${nc}`);
            queue.push([nr, nc]);
        }
        
    }
    
    
    return found ? traces[exitR][exitC] : -1;
}