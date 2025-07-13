from collections import deque

def solution(park, routes):
    H, W = len(park), len(park[0])
    cur_r, cur_c = 0, 0
    found = False
    
    for r in range(H):
        for c in range(W):
            if park[r][c] == 'S':
                cur_r, cur_c = r, c
                found = True
                break
        if found:
            break
        
    q = deque([])    
    
    # N S W E
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def get_dir(ch):
        if ch == 'N':
            return 0
        elif ch == 'S':
            return 1
        elif ch == 'W':
            return 2
        else:
            return 3
        
    def bfs(cur_r, cur_c, direction, cnt):
        q.append((cur_r, cur_c, direction, cnt))

        while q:
            r, c, d, k = q.popleft()
            
            if k <= 0:
                return (r, c)
            
            dr, dc = dir[get_dir(d)]
            nr, nc = dr + r, dc + c
                
            if nr < 0 or nr >= H or nc < 0 or nc >= W or park[nr][nc] == 'X':
                continue
                    
            q.append((nr, nc, d, k-1))
              
        return (cur_r, cur_c)        
                
    for route in routes:
        direction, cnt = route[0], int(route[2])
        cur_r, cur_c = bfs(cur_r, cur_c, direction, cnt)
        
        
    return [cur_r, cur_c]