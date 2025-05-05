function solution(n, wires) {
    const adj = Array.from({length: n + 1}, () => []);

    for (const [from, to] of wires) {
        adj[from].push(to);
        adj[to].push(from);
    }

    function dfs(node, visited) {
        visited.add(node);
        let count = 1; 

        for (const next of adj[node]) {
            if (!visited.has(next)) {
                count += dfs(next, visited);
            }
        }
        return count;
    }

    let minDiff = n;

    for (const [from, to] of wires) {
        // 간선 제거
        adj[from] = adj[from].filter(v => v !== to);
        adj[to] = adj[to].filter(v => v !== from);

        const visited = new Set();
        const size = dfs(from, visited);
        const diff = Math.abs((n - size) - size);
        minDiff = Math.min(minDiff, diff);

        // 간선 복원
        adj[from].push(to);
        adj[to].push(from);
    }

    return minDiff;
}
