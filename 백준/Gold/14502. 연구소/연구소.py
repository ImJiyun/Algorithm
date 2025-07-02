import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]
cells = []
virus = []

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for r in range(N):
    for c in range(M):
        if grid[r][c] == 0:
            cells.append((r, c))
        elif grid[r][c] == 2:
            virus.append((r, c))
          
def bfs():
    copy = [row[:] for row in grid]
    q = deque(virus)
    while q:
        r, c = q.popleft()
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr > N-1 or nc < 0 or nc > M-1 or copy[nr][nc] != 0:
                continue
            copy[nr][nc] = 2
            q.append((nr, nc))

    safe = sum(row.count(0) for row in copy)
    return safe

max_safe = 0
def build_walls(idx, n):
    global max_safe
    if n == 3:
        result = bfs()
        max_safe = max(max_safe, result)
        return 
    
    for i in range(idx, len(cells)):
        r, c = cells[i]
        grid[r][c] = 1
        build_walls(i+1, n+1)
        grid[r][c] = 0
        
build_walls(0, 0)        
print(max_safe)       