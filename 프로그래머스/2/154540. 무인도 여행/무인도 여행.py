import sys
sys.setrecursionlimit(10**6)

def solution(maps):
    R = len(maps)
    C = len(maps[0])
    dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    ans = []
    
    visited = [[False] * C for _ in range(R)]
    
    def dfs(r, c):
        visited[r][c] = True
        cnt[0] += int(maps[r][c])
        
        for dr, dc in dir:
            nr = r + dr
            nc = c + dc
            
            if nr < 0 or nr >= R or nc < 0 or nc >= C or visited[nr][nc] or maps[nr][nc] == 'X':
                continue
            dfs(nr, nc)
            
    for r in range(R):
        for c in range(C):
            if maps[r][c] != 'X' and not visited[r][c]:
                cnt = [0]
                dfs(r, c)
                ans.append(cnt[0])
        
    ans.sort()
    
    return ans if len(ans) > 0 else [-1]