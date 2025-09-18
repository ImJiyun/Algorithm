from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    from collections import deque

def solution(rectangles, characterX, characterY, itemX, itemY):
    SCALE = 2
    rects = [[x1*SCALE, y1*SCALE, x2*SCALE, y2*SCALE] for x1,y1,x2,y2 in rectangles]
    sx, sy = characterX*SCALE, characterY*SCALE
    tx, ty = itemX*SCALE, itemY*SCALE

    MAX = 102 * SCALE
    board = [[0]* (MAX+1) for _ in range(MAX+1)]

    for x1, y1, x2, y2 in rects:
        for x in range(x1, x2+1):
            board[y1][x] = 1
            board[y2][x] = 1
        for y in range(y1, y2+1):
            board[y][x1] = 1
            board[y][x2] = 1

    for x1, y1, x2, y2 in rects:
        for y in range(y1+1, y2):
            for x in range(x1+1, x2):
                board[y][x] = 0

    q = deque([(sy, sx, 0)]) 
    visited = [[False]*(MAX+1) for _ in range(MAX+1)]
    visited[sy][sx] = True
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]

    while q:
        y, x, d = q.popleft()
        if (y, x) == (ty, tx):
            return d // 2  

        for dy, dx in dirs:
            ny, nx = y+dy, x+dx
            if 0 <= ny <= MAX and 0 <= nx <= MAX and not visited[ny][nx]:
                if board[ny][nx] == 1: 
                    visited[ny][nx] = True
                    q.append((ny, nx, d+1))

    return -1  

