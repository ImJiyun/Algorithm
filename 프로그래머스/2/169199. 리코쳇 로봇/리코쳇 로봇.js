function solution(board) {
    const dir = [[-1, 0], [0, -1], [1, 0], [0, 1]];
    let robotR, robotC, destR, destC;
    
    board = board.map(row => row.split(""));
    
    for (let r = 0; r < board.length; r++) {
        for (let c = 0; c < board[0].length; c++) {
            if (board[r][c] === "R") {
                robotR = r;
                robotC = c;
            }
            if (board[r][c] === "G") {
                destR = r;
                destC = c;
            }
        }
    }

    const visited = Array.from({length : board.length}, () => Array(board[0].length).fill(false));
    const queue = [[robotR, robotC, 0]];
    visited[robotR][robotC] = true;
    
    while (queue.length > 0) {
        const [curR, curC, count] = queue.shift();
        
        for (let d = 0; d < dir.length; d++) {
            let nr = curR;
            let nc = curC;
            
            while (true) {
                let tr = nr + dir[d][0];
                let tc = nc + dir[d][1];
                
                if (tr < 0 || tc < 0 || tr >= board.length || tc >= board[0].length || board[tr][tc] === 'D') break;
                nr = tr;
                nc = tc;
            }
            
            if (visited[nr][nc]) continue;
            if (nr === destR && nc === destC) return count + 1;
            
            visited[nr][nc] = true;
            queue.push([nr, nc, count + 1]);
        }
    }
    return -1;
}