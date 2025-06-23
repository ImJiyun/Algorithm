import sys
from collections import deque
input = sys.stdin.readline

board = [list(input().split()) for _ in range(5)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ans = []

def bfs(d):
    while len(d) > 0:
        r, c, l = d.popleft()
        if len(l) == 6:
            if l not in ans:
                ans.append(l)
            continue
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if nr < 0 or nc < 0 or nr >= 5 or nc >= 5:
                continue
            d.append((nr, nc, l + board[nr][nc]))    
            
for r in range(5):
    for c in range(5):
        d = deque([(r, c, board[r][c])])
        bfs(d)
        
print(len(ans))    