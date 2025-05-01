function solution(m, n, puddles) {
    const arr = Array.from({length: n}, () => Array(m).fill(0));
    const MOD = 1000000007;
    
    for (let [x, y] of puddles) {
        arr[y-1][x-1] = -1;
    }
    
    if (arr[0][0] !== -1) arr[0][0] = 1;
    
    for (let r = 0; r < n; r++) {
        for (let c = 0; c < m; c++) {
            if (arr[r][c] === -1) {
                arr[r][c] = 0;
                continue;
            }
            if (r > 0) arr[r][c] += arr[r-1][c];
            if (c > 0) arr[r][c] += arr[r][c-1];
            arr[r][c] %= MOD;
        }
    }
    
    return arr[n-1][m-1];
}