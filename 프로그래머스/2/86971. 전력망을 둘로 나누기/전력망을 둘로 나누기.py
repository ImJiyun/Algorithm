def solution(n, wires):
    graph = [[0] * (n+1) for _ in range(n+1)]
    
    for a, b in wires:
        graph[a][b] = graph[b][a] = 1
    
    minDiff = n
    
    def dfs(r, c):
        cnt[0] += 1
        visited[r][c] = visited[c][r] = True
        
        for i, nxt in enumerate(graph[c]):
            if nxt == 1 and not visited[c][i]:
                dfs(c, i)
    
    for r in range(n+1):
        for c in range(n+1):
            if graph[r][c] == 0:
                continue
            graph[r][c] = graph[c][r] = 0
            visited = [[False] * (n+1) for _ in range(n+1)]
            cnt = [0]
            dfs(r, c)
            minDiff = min(minDiff, abs(2 * cnt[0] -n))
            graph[r][c] = graph[c][r] = 1
            
    return minDiff