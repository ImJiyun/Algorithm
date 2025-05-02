function solution(maps) {
    const answer = [];
    const R = maps.length;
    const C = maps[0].length;
    
    let found = false;
    
    for (let i = 0; i < R; i++) {
        const rows = maps[i].split('');
        for (let j = 0; j < rows.length; j++) {
            if (rows[j] !== 'X') {
                rows[j] = Number(rows[j]);
                found = true;
            }
        }   
        maps[i] = rows;
    }
    
    if (!found) return [-1];
    
    const dir = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    const visited = new Set();
    let sum;
    
    function dfs(r, c) {
        visited.add(`${r},${c}`);
        sum += maps[r][c];
        
        for (let [dr, dc] of dir) {
            const nr = dr + r;
            const nc = dc + c;
            
            if (nr < 0 || nr >= R || nc < 0 || nc >= C || visited.has(`${nr},${nc}`)) continue;
            if (maps[nr][nc] === 'X') continue;
            dfs(nr, nc);
        }
    }
    
    for (let r = 0; r < R; r++) {
        for (let c = 0; c < C; c++) {
            if (maps[r][c] !== 'X' && !visited.has(`${r},${c}`)) {
                sum = 0;
                dfs(r, c);
                answer.push(sum);
            }
        }
    }
    
    return answer.sort((a,b) => a-b);
}