from collections import deque

def solution(board):
    R = len(board)
    C = len(board[0])
    dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    visited = [[False] * C for _ in range(R)]
    strR, strC = 0, 0
    endR, endC = 0, 0
    
    for r in range(R):
        for c in range(C):
            if board[r][c] == 'R':
                strR, strC = r, c
            if board[r][c] == 'G':
                endR, endC = r, c
    
    q = deque([(strR, strC, 0)])
    visited[strR][strC] = True
    
    while q:
        r, c, mov = q.popleft()
        
        if r == endR and c == endC:
            return mov
        
        for dr, dc in dir:
            i = 1
            tr, tc = r, c
            while True:
                tr = r + dr * i
                tc = c + dc * i
                if tr < 0 or tr >= R or tc < 0 or tc >= C or board[tr][tc] == 'D':
                    tr, tc = r + dr * (i-1), c + dc * (i-1)
                    break
                i += 1
            nr, nc = tr, tc
            if not visited[nr][nc]:
                visited[nr][nc] = True    
                q.append((nr, nc, mov + 1))
    
    return -1