function solution(n, computers) {
    let count = 0;
    const visited = new Set();
    
    function dfs(node) {
        visited.add(node);
        for (let i = 0; i < computers[node].length; i++) {
            if (node === i) continue;
            if (!visited.has(i) && computers[node][i] === 1) dfs(i);
        }
    }
    
    for (let i = 0; i < n; i++) {
        if (visited.has(i)) continue;
        count++;
        dfs(i);
    }
    
    return count;
}