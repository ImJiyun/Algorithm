# from collections import deque

# def solution(maps):
#     dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
#     n = len(maps)
#     m = len(maps[0])
#     visited = set([(0, 0)])
    
#     queue = deque([(0, 0, 1)])
    
#     while (len(queue) > 0):
#         r, c, k = queue.popleft()
        
#         if r == n - 1 and c == m - 1:
#             return k
        
#         for dr, dc in dir:
#             nr = r + dr
#             nc = c + dc
            
#             if nr < 0 or nc < 0 or nr > n-1 or nc > m-1 or (nr, nc) in visited:
#                 continue
#             if maps[nr][nc] == 0:
#                 continue
#             visited.add((nr, nc))
#             queue.append((nr, nc, k+1))
            
#     return -1

from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    
    q = deque([(0,0)])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    while True:
        if len(q) == 0: return -1
        
        r, c = q.popleft()
        
        if r == n-1 and c == m-1: break
        
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            
            if nr < 0 or nr >= n or nc < 0 or nc >= m or maps[nr][nc] == 0 or visited[nr][nc]:
                continue
            visited[nr][nc] = True
            maps[nr][nc] += maps[r][c]
                            
            q.append((nr, nc))
    
    return maps[n-1][m-1] 