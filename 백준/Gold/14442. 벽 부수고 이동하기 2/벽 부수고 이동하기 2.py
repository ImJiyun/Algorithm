import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
grid = [input().strip() for _ in range(N)]

INF = K + 1
best = [[INF] * M for _ in range(N)]
best[0][0] = 0

q = deque()
q.append((0, 0, 0, 1)) # r, c, breaks, dist
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

ans = -1
while q:
    r, c, b, d = q.popleft()
    if r == N-1 and c == M-1:
        ans = d
        break
        
    for dr, dc in dirs:
        nr, nc = r+dr, c+dc
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        if grid[nr][nc] == '0':
            nb = b
        else:
            nb = b+1
            if nb > K:
                continue
        if nb < best[nr][nc]:
            best[nr][nc] = nb
            q.append((nr, nc, nb, d+1))
            
print(ans)