function solution(n, edge) {
    let answer = 0;
    const map = new Map();
    const visited = new Set();
    
    for (let [n1, n2] of edge) {
        if (!map.has(n1)) map.set(n1, []);
        if (!map.has(n2)) map.set(n2, []);
        map.get(n1).push(n2);
        map.get(n2).push(n1);
    }
    
    const queue = [1];
    let distance = 1;
    visited.add(1);
    const dist = new Array(n + 1).fill(0);
    
    while (queue.length > 0) {
        const popped = queue.shift();
        
        for (let node of map.get(popped)) {
            if (!visited.has(node)) {
                queue.push(node);
                visited.add(node);
                dist[node] = dist[popped] + 1;
            }
        }
    }
    
    const max = Math.max(...dist);
    return dist.filter(value => value === max).length;
}