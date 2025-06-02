def solution(n, computers):
    cnt = 0
    visited = [False] * n
    
    def dfs(node):
        visited[node] = True
        
        for i, nxt in enumerate(computers[node]):
            if nxt == 1 and not visited[i]:
                dfs(i)
    
    for i in range(n):
        if not visited[i]:
            cnt += 1
            dfs(i)
            
    return cnt