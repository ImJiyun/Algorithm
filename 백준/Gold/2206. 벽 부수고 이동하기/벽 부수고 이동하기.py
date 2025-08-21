import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

map = [list(map(int, input().strip())) for _ in range(N)]

visited = [[[False]*2 for _ in range(M)] for _ in range(N)]
dq = deque()
dq.append((0, 0, 0, 1)) # r, c, broken, dist
visited[0][0][0] = True

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

ans = -1

while dq:
    r, c, b, d = dq.popleft()
    if r == N-1 and c == M-1:
        ans = d
        break
    for dr, dc in dir:
        nr, nc = r+dr, c+dc
        if 0 <= nr < N and 0 <= nc < M:
            if map[nr][nc] == 0 and not visited[nr][nc][b]:
                visited[nr][nc][b] = True
                dq.append((nr, nc, b, d+1))
            elif map[nr][nc] == 1 and b == 0 and not visited[nr][nc][1]:
                visited[nr][nc][1] = True
                dq.append((nr, nc, 1, d+1))
print(ans)