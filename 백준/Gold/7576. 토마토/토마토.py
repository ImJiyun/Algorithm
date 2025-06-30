import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

q = deque([])

for r in range(N):
    for c in range(M):
        if grid[r][c] == 1:
            q.append((r, c, 0))
            
ans = 0

while q:
    r, c, d = q.popleft()
    ans = max(ans, d)
    
    for dr, dc in dir:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= N or nc < 0 or nc >= M or grid[nr][nc] != 0:
            continue
        grid[nr][nc] = d + 1
        q.append((nr, nc, d + 1))
        
for r in range(N):
    for c in range(M):
        if grid[r][c] == 0:
            ans = -1
            break
            
print(ans)            