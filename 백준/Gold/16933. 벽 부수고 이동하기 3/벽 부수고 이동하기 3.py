import sys
from collections import deque

input = sys.stdin.readline
N, M, K = map(int, input().split())
grid = [input().strip() for _ in range(N)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

INF = K+1
best = [[[INF, INF] for _ in range(M)] for _ in range(N)]
best[0][0][1] = 0
q = deque([(0, 0, 0, 1)])

ans = -1
while q:
    r, c, b, d = q.popleft()
    day = 1 if d%2 == 1 else 0
    
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
            if day == 0:
                continue
            nb = b+1
            if nb > K:
                continue
        nd = 1 - day
        if nb < best[nr][nc][nd]:
            best[nr][nc][nd] = nb
            q.append((nr, nc, nb, d+1))
    nd = 1 - day
    if b < best[r][c][nd]:
        best[r][c][nd] = b
        q.append((r, c, b, d + 1))   
print(ans)