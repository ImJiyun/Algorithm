import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

day = 0 

def bfs(start_r, start_c, visited):
    q = deque([(start_r, start_c)])
    connected = [(start_r, start_c)]
    visited[start_r][start_c] = True
    total_pop = grid[start_r][start_c]
    
    while q:
        r, c = q.popleft()
        
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                dist = abs(grid[nr][nc] - grid[r][c])
                if L <= dist <= R:
                    visited[nr][nc] = True    
                    connected.append((nr, nc))
                    q.append((nr, nc))
            
    if len(connected) > 1:
        new_pop = sum(grid[r][c] for r, c in connected) // len(connected)
        for r, c in connected:
            grid[r][c] = new_pop
        return True
    return False
        
while True:
    visited = [[False] * N for _ in range(N)]
    moved = False
    
    for r in range(N):
        for c in range(N):
            if visited[r][c]:
                continue
            if bfs(r, c, visited):
                moved = True
    
    if not moved:
        break
    day += 1        
            
print(day)            